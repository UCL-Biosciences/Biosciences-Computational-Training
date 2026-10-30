# Steps to setting up VS Code for the CS Cluster

The recent versions of VS Code are currently not supported on the CS Cluster's Operating System, only VS Code version 1.98.0 or below would work. 

**The simplest solution is to download an older version of VS Code, available at: https://code.visualstudio.com/updates/archive**

However, if using the latest version of VS Code is preferred, follow the below instructions:

1. Go to the release page of [hsfzxjy/vscode-remote-glibc-patch](https://github.com/hsfzxjy/vscode-remote-glibc-patch/releases/tag/BUILD)

2. If you are not sure about the Linux kernel version you are using, you can use the following command to check the usage:

```sh
$ uname -r 
3.10.0-1160.88.1.el7.x86_64
```

For example, on CentOS 7, you should download the file named `x86_64-kernel-3.4.113-gcc-8.5.0-glibc-2.28.tgz` under your kernel version in the [Release](https://github.com/hsfzxjy/vscode-remote-glibc-patch/releases/tag/BUILD) page.

To download the build directly to the cluster, follow the below command:

```sh
$ wget https://github.com/hsfzxjy/vscode-remote-glibc-patch/releases/download/BUILD/x86_64-kernel-3.4.113-gcc-8.5.0-glibc-2.28.tgz
```

3. Create a directory named `vscode-sysroot`

```sh
$ mkdir vscode-sysroot
```

4. Extract the `.tgz` file using the command:

```sh
$ tar -xzf x86_64-kernel-3.4.113-gcc-8.5.0-glibc-2.28.tgz
```

After extraction, the directory would look as follows:

```
.
├── x86_64-linux-gnu/
├── init.sh*
├── patchelf*
└── x86_64-kernel-3.4.113-gcc-8.5.0-glibc-2.28.tgz
```

5. In the terminal, enter the following commands:

```sh
$ echo 'eval "$(/home/<your-username>/vscode-sysroot/init.sh)"' >> ~/.bash_profile
$ echo 'eval "$(/home/<your-username>/vscode-sysroot/init.sh)"' >> ~/.bashrc
```

This will add necessary commands to `.bash_profile` and `.bashrc` so that `~/vscode-sysroot/init.sh` runs automatically at startup.

4. Since `init.sh` has not been executed the first time, load `.bash_profile` with the following command to run `init.sh` and manually set the environment variables related to VS Code:

```sh
source ~/.bash_profile
```

