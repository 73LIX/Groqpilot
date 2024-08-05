@echo off
setlocal

echo Checking Python installation...

python --version >nul 2>&1
IF %ERRORLEVEL% NEQ 0 (
    echo Python is not installed. Downloading and installing Python 3.10.11...

    :: Download Python installer
    powershell -Command "Invoke-WebRequest -Uri https://www.python.org/ftp/python/3.10.11/python-3.10.11-amd64.exe -OutFile python-3.10.11-amd64.exe"

    :: Run the installer
    start /wait python-3.10.11-amd64.exe /quiet InstallAllUsers=1 PrependPath=1

    :: Deleting installer
    del python-3.10.11-amd64.exe >nul 2>&1

    :: Check installation again
    python --version >nul 2>&1
    IF %ERRORLEVEL% NEQ 0 (
        echo Python installation failed. Please install Python manually and try again.
        pause
        exit /b
    )
)

echo Python is installed. Setting up the environment...

:: Create a virtual environment
python -m venv venv
:: Check if the virtual environment was created successfully
if exist venv (
    echo Virtual environment created successfully.
) else (
    echo Error: Failed to create virtual environment.
    pause
    exit /b
)

:: Activate the virtual environment
call venv\Scripts\activate

:: Upgrade pip and setuptools
python.exe -m pip install --upgrade pip setuptools >nul 2>&1
python.exe -m spacy download en_core_web_sm >nul
if %errorlevel% neq 0 (
    echo Error downloading Spacy model
    exit /b 1
)

:: Check for dependencies
echo Checking for updates...
set DEPENDENCIES_INSTALLED=true
for /F "delims=" %%i in (requirements.txt) do (
pip list %%i 2>&1 | findstr /i "%%i" >nul || (
        set DEPENDENCIES_INSTALLED=false
    )
)

:: Installing dependencies if not
if "%DEPENDENCIES_INSTALLED%"=="false" (
    echo Installing dependencies...
    pip install -r requirements.txt >nul 2>&1
)

:: If dependencies are already installed, skip to next step
if "%DEPENDENCIES_INSTALLED%"=="true" (
    goto :skip_install
)

:: Create 'secrets' directory if it does not exist
:skip_install
if not exist secrets (
    mkdir secrets
)

:: Check if the API key file exists inside 'secrets' folder
if exist secrets\api_key.txt (
    :: Read API key from file
    set /p GROQ_API_KEY=<secrets\api_key.txt
) else (
    :enter_api_key
    echo Enter your GROQ API Key:
    set /p GROQ_API_KEY=

    :: Check if API key is empty
    if "%GROQ_API_KEY%"=="" (
        echo Error: API Key is required, Try again.
        goto enter_api_key
    )

    :: Save API key to the txt file inside 'secrets' folder
    echo %GROQ_API_KEY% > secrets\api_key.txt
)

:: Model Dropdown
echo Choose a model by entering the corresponding number, or type in your own model:
echo 1. llama-3.1-70b-versatile
echo 2. mixtral-8x7b-32768
echo 3. gemma2-9b-it
echo 4. Type in your own Model ID from groq
echo Press Enter to use the default model(Llama-3.1-70B).
set /p MODEL_CHOICE=Enter the number for your model choice or type in your model:

:: Set the default model if presses enter
set MODEL_NAME=llama-3.1-70b-versatile

:: Update MODEL_NAME based on the user's choice
if "%MODEL_CHOICE%"=="1" set MODEL_NAME=llama-3.1-70b-versatile
if "%MODEL_CHOICE%"=="2" set MODEL_NAME=mixtral-8x7b-32768
if "%MODEL_CHOICE%"=="3" set MODEL_NAME=gemma2-9b-it
if "%MODEL_CHOICE%"=="4" (
    echo Enter your model name:
    set /p MODEL_NAME=
)

:: Ensure MODEL_NAME is set without failure
if "%MODEL_NAME%"=="" set MODEL_NAME=llama-3.1-70b-versatile

echo Selected model: %MODEL_NAME%

echo Starting the application...

:: Run the Gradio app in the background and capture its PID
start /b python app.py %GROQ_API_KEY% %MODEL_NAME%

:: Retrieve PID of the Gradio process
for /f "tokens=2" %%i in ('tasklist ^| findstr /i "python.exe"') do set PID=%%i

:: Wait a bit to ensure the server starts up
timeout /t 7 /nobreak >nul

:: Open the Gradio URL in the default browser
start http://127.0.0.1:7860

:: Prompt user to type "exit" to stop the Gradio app and exit
:wait_for_exit
echo Type the word "exit" and press Enter to stop the Gradio app.

:: enter exit here to close the app
:input_loop
set /p user_input= 
if /i "%user_input%"=="exit" (
    :: Terminate the Gradio process
    taskkill /pid %PID% /f >nul 2>&1
    goto :end
) else (
    echo Invalid input. Please type "exit" to stop the Gradio app and exit.
    goto :input_loop
)

:end
:: Deactivate the virtual environment after the app is closed
deactivate

exit /b
