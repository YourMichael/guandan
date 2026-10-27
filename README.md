# Q萌掼蛋 安卓 App

单机版 Q 版掼蛋。把这个仓库推到 GitHub，GitHub 会自动把游戏打包成安卓安装包（APK）。

## 目录说明

- `www/index.html`：游戏本体。以后改游戏，只要替换这个文件。
- `resources/android/res/`：App 图标和启动图。
- `resources/debug.keystore`：固定签名，保证新版本能直接覆盖安装旧版本。
- `.github/workflows/build-android.yml`：自动打包流程。
- `scripts/bundle_fonts.py`：打包时把可爱字体下载进 App，断网也能正常显示。

## 下载安装包

1. 打开仓库的 **Actions** 页面，等「打包安卓 App」变成绿色对勾（约 5～8 分钟）。
2. 打开仓库首页右侧的 **Releases**，下载最新版里的 `QMengGuandan.apk`。
3. 用安卓手机安装。如果手机提示「禁止安装未知来源应用」，按提示允许一次即可。

## 更新游戏

在 GitHub 网页上打开 `www/index.html`，点右上角的铅笔图标，或者上传新文件覆盖它，然后提交。GitHub 会自动重新打包，Releases 里会多出一个新版本。

## 说明

- 安装包为调试签名，适合自己和朋友安装，不能直接上架应用商店。上架需要另做正式签名。
- 修改 `capacitor.config.json` 里的 `appName` 可以改 App 名称；不要改 `appId`，否则会被手机当作另一个 App。
