# GitHub上传指南 📚

本文档将指导您如何将Python PyTorch学习项目上传到GitHub。

## 📋 准备工作

### 1. 安装Git
如果您还没有安装Git，请按照以下步骤：

1. 访问 [Git官网](https://git-scm.com/download/win)
2. 下载Windows版Git
3. 运行安装程序，使用默认设置即可
4. 安装完成后重启VS Code

### 2. 配置Git用户信息
首次使用Git需要配置用户信息：

```bash
git config --global user.name "您的姓名"
git config --global user.email "您的邮箱@example.com"
```

### 3. 创建GitHub仓库
1. 登录 [GitHub](https://github.com)
2. 点击右上角的 "+" 号，选择 "New repository"
3. 仓库名称输入：`pytorch_learning`
4. 描述输入：`Python和PyTorch深度学习完整教程`
5. 选择 "Public"（公开）
6. **不要**勾选 "Add a README file"（我们已经有了）
7. 点击 "Create repository"

## 🚀 上传方法

### 方法一：使用批处理脚本（推荐）

1. 双击运行 `upload_to_github.bat` 文件
2. 按照提示操作
3. 如果需要认证，输入您的GitHub用户名和密码/Token

### 方法二：手动使用Git命令

在VS Code的终端中依次执行：

```bash
# 1. 初始化Git仓库
git init

# 2. 添加所有文件
git add .

# 3. 提交文件
git commit -m "初始提交: Python和PyTorch深度学习完整教程"

# 4. 设置主分支
git branch -M main

# 5. 添加远程仓库
git remote add origin https://github.com/Atn0s/pytorch_learing.git

# 6. 推送到GitHub
git push -u origin main
```

## 🔐 认证方式

### Personal Access Token（推荐）

1. 访问 GitHub Settings > Developer settings > Personal access tokens
2. 点击 "Generate new token"
3. 选择适当的权限（至少需要 repo 权限）
4. 复制生成的token
5. 在Git要求密码时，输入token而不是密码

### SSH密钥（高级用户）

如果您熟悉SSH，可以设置SSH密钥来避免每次输入密码。

## 📝 后续更新

项目上传成功后，如果需要更新代码：

```bash
# 添加修改的文件
git add .

# 提交更改
git commit -m "更新描述"

# 推送到GitHub
git push
```

## 🚨 常见问题

### Q: 推送时提示认证失败？
A: 确保您的GitHub用户名和密码/Token正确。注意：GitHub已不支持密码认证，请使用Personal Access Token。

### Q: 提示仓库不存在？
A: 检查仓库URL是否正确，确保仓库已在GitHub上创建。

### Q: 文件太大无法上传？
A: GitHub单文件限制100MB，仓库大小限制1GB。如有大文件，考虑使用Git LFS。

### Q: 中文文件名显示乱码？
A: 执行 `git config --global core.quotepath false` 解决。

## 📞 获取帮助

如果遇到问题，可以：
1. 查看Git/GitHub官方文档
2. 在项目中提交Issue
3. 搜索Stack Overflow相关问题

---

祝您上传成功！🎉
