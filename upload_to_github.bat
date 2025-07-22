@echo off
echo ========================================
echo  上传Python PyTorch学习项目到Gitee
echo ========================================
echo.

REM 检查Git是否已安装
git --version >nul 2>&1
if %errorlevel% neq 0 (
    echo [错误] Git未安装或未在PATH中！
    echo 请先安装Git: https://git-scm.com/download/win
    echo 安装完成后重新运行此脚本。
    pause
    exit /b 1
)

echo [信息] Git已安装，开始上传流程...
echo.

REM 初始化Git仓库
echo [步骤1] 初始化Git仓库...
git init
if %errorlevel% neq 0 (
    echo [错误] Git初始化失败！
    pause
    exit /b 1
)

REM 添加所有文件
echo [步骤2] 添加文件到Git...
git add .
if %errorlevel% neq 0 (
    echo [错误] 添加文件失败！
    pause
    exit /b 1
)

REM 提交文件
echo [步骤3] 提交文件...
git commit -m "初始提交: Python和PyTorch深度学习完整教程"
if %errorlevel% neq 0 (
    echo [错误] 提交文件失败！
    pause
    exit /b 1
)

REM 设置主分支
echo [步骤4] 设置主分支...
git branch -M main
if %errorlevel% neq 0 (
    echo [警告] 设置主分支失败，但可以继续...
)

REM 添加远程仓库
echo [步骤5] 添加远程仓库...
git remote add origin https://gitee.com/Atnn0s/pytorch_learning.git
if %errorlevel% neq 0 (
    echo [错误] 添加远程仓库失败！
    echo 请检查GitHub仓库地址是否正确。
    pause
    exit /b 1
)

REM 推送到Gitee
echo [步骤6] 推送到Gitee...
echo 注意: 首次推送可能需要您输入Gitee用户名和密码
git push -u origin main
if %errorlevel% neq 0 (
    echo [错误] 推送失败！
    echo 可能的原因:
    echo 1. 网络连接问题
    echo 2. GitHub认证问题
    echo 3. 仓库不存在或无权限
    echo.
    echo 请检查以上问题后重试。
    pause
    exit /b 1
)

echo.
echo ========================================
echo          上传成功！🎉
echo ========================================
echo.
echo 您的项目已成功上传到:
echo https://gitee.com/Atnn0s/pytorch_learning
echo.
echo 下次更新代码时，可以使用以下命令:
echo git add .
echo git commit -m "更新描述"
echo git push
echo.
pause
