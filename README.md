# LIBCURL 7.54.1 (No SSL)
[https://github.com/curl/curl](https://github.com/curl/curl)   
  
[__ZLIB__](http://www.zlib.net/) - Copyright (C)1995-2017 Jean-loup Gailly and Mark Adler   
   
**TARGETS**   
* windows-Win32-v120 (Visual Studio 2013)   
* windows-x64-v120 (Visual Studio 2013)   
* windows-Win32-v140 (Visual Studio 2015)   
* windows-x64-v140 (Visual Studio 2015)   
* windows-Win32-v141 (Visual Studio 2017)   
* windows-x64-v141 (Visual Studio 2017)   
* linux-i686 (gcc-4.9)   
* linux-x86_64 (gcc-4.9)   
* linux-armel (gcc-4.9)   
* linux-armhf (gcc-4.9)   
* linux-aarch64 (gcc-4.9)   
* android-armeabi-v7a (ndk-r12b/api-21)   
* android-arm64-v8a (ndk-r12b/api-21)  
* android-x86 (ndk-r12b/api-21)  
   
**BUILD ENVIRONMENT**  
* Windows 10 x64 15063   
* Visual Studio 2013
* Visual Studio 2015 (with Git for Windows)   
* Bash on Ubuntu on Windows 16.04.1 LTS   
  
**CONFIGURE BASH ON UBUNTU ON WINDOWS**   
Open "Bash on Ubuntu on Windows"   
```
sudo dpkg --add-architecture i386
sudo apt-get update
sudo apt-get install gcc-4.9 g++-4.9 libc6-dev:i386 libstdc++-4.9-dev:i386 lib32gcc-4.9-dev 
sudo apt-get install gcc-4.9-arm-linux-gnueabihf g++-4.9-arm-linux-gnueabihf gcc-4.9-arm-linux-gnueabi g++-4.9-arm-linux-gnueabi gcc-4.9-aarch64-linux-gnu g++-4.9-aarch64-linux-gnu
sudo apt-get install autoconf libtool make p7zip-full python
```
   
**CONFIGURE ANDROID TOOLCHAINS**   
Open "Bash on Ubuntu on Windows"   
```
wget https://dl.google.com/android/repository/android-ndk-r12b-linux-x86_64.zip
7z x android-ndk-r12b-linux-x86_64.zip
android-ndk-r12b/build/tools/make_standalone_toolchain.py --arch arm --api 21 --stl gnustl --install-dir ./arm-linux-androideabi
android-ndk-r12b/build/tools/make_standalone_toolchain.py --arch arm64 --api 21 --stl gnustl --install-dir ./aarch64-linux-android
android-ndk-r12b/build/tools/make_standalone_toolchain.py --arch x86 --api 21 --stl gnustl --install-dir ./i686-linux-android
```
  
**BUILD LIBCURL (windows-Win32-v120)**  
Open "VS2013 x86 Native Tools Command Prompt"   
```
git clone https://github.com/curl/curl.git -b curl-7_54_1 --depth=1
cd curl\winbuild
nmake /f Makefile.vc mode=static VC=12 DEBUG=no MACHINE=x86 ENABLE_WINSSL=no
nmake /f Makefile.vc mode=static VC=12 DEBUG=yes MACHINE=x86 ENABLE_WINSSL=no
```
Get header files from builds\libcurl-vc12-x86-release-static-ipv6-sspi\include   
Get libcurl_a.lib from builds\libcurl-vc12-x86-release-static-ipv6-sspi\lib    
Get libcurl_a_debug.lib from builds\libcurl-vc12-x86-debug-static-ipv6-sspi\lib    
   
**BUILD LIBCURL (windows-x64-v120)**  
Open "VS2013 x64 Native Tools Command Prompt"    
```
git clone https://github.com/curl/curl.git -b curl-7_54_1 --depth=1
cd curl\winbuild
nmake /f Makefile.vc mode=static VC=12 DEBUG=no MACHINE=x64 ENABLE_WINSSL=no
nmake /f Makefile.vc mode=static VC=12 DEBUG=yes MACHINE=x64 ENABLE_WINSSL=no
```
Get header files from builds\libcurl-vc12-x64-release-static-ipv6-sspi\include   
Get libcurl_a.lib from builds\libcurl-vc12-x64-release-static-ipv6-sspi\lib    
Get libcurl_a_debug.lib from builds\libcurl-vc12-x64-debug-static-ipv6-sspi\lib    
   
**BUILD LIBCURL (windows-Win32-v140)**  
Open "VS2015 x86 Native Tools Command Prompt"   
```
git clone https://github.com/curl/curl.git -b curl-7_54_1 --depth=1
cd curl\winbuild
nmake /f Makefile.vc mode=static VC=14 DEBUG=no MACHINE=x86 ENABLE_WINSSL=no
nmake /f Makefile.vc mode=static VC=14 DEBUG=yes MACHINE=x86 ENABLE_WINSSL=no
```
Get header files from builds\libcurl-vc14-x86-release-static-ipv6-sspi\include   
Get libcurl_a.lib from builds\libcurl-vc14-x86-release-static-ipv6-sspi\lib    
Get libcurl_a_debug.lib from builds\libcurl-vc14-x86-debug-static-ipv6-sspi\lib    
   
**BUILD LIBCURL (windows-x64-v140)**  
Open "VS2015 x64 Native Tools Command Prompt"    
```
git clone https://github.com/curl/curl.git -b curl-7_54_1 --depth=1
cd curl\winbuild
nmake /f Makefile.vc mode=static VC=14 DEBUG=no MACHINE=x64 ENABLE_WINSSL=no
nmake /f Makefile.vc mode=static VC=14 DEBUG=yes MACHINE=x64 ENABLE_WINSSL=no
```
Get header files from builds\libcurl-vc14-x64-release-static-ipv6-sspi\include   
Get libcurl_a.lib from builds\libcurl-vc14-x64-release-static-ipv6-sspi\lib    
Get libcurl_a_debug.lib from builds\libcurl-vc14-x64-debug-static-ipv6-sspi\lib    

**BUILD LIBCURL (windows-Win32-v141)**  
Open "x86 Native Tools Command Prompt for VS2017"    
```
git clone https://github.com/curl/curl.git -b curl-7_54_1 --depth=1
cd curl\winbuild
nmake /f Makefile.vc mode=static VC=14 DEBUG=no MACHINE=x86 ENABLE_WINSSL=no
nmake /f Makefile.vc mode=static VC=14 DEBUG=yes MACHINE=x86 ENABLE_WINSSL=no
```
Get header files from builds\libcurl-vc14-x86-release-static-ipv6-sspi\include   
Get libcurl_a.lib from builds\libcurl-vc14-x86-release-static-ipv6-sspi\lib    
Get libcurl_a_debug.lib from builds\libcurl-vc14-x86-debug-static-ipv6-sspi\lib    
   
**BUILD LIBCURL (windows-x64-v141)**  
Open "x64 Native Tools Command Prompt for VS2017"    
```
git clone https://github.com/curl/curl.git -b curl-7_54_1 --depth=1
cd curl\winbuild
nmake /f Makefile.vc mode=static VC=14 DEBUG=no MACHINE=x64 ENABLE_WINSSL=no
nmake /f Makefile.vc mode=static VC=14 DEBUG=yes MACHINE=x64 ENABLE_WINSSL=no
```
Get header files from builds\libcurl-vc14-x64-release-static-ipv6-sspi\include   
Get libcurl_a.lib from builds\libcurl-vc14-x64-release-static-ipv6-sspi\lib    
Get libcurl_a_debug.lib from builds\libcurl-vc14-x64-debug-static-ipv6-sspi\lib    

**BUILD LIBCURL (linux-i686)**   
Open "Bash on Ubuntu on Windows"   
```
git clone https://github.com/djp952/prebuilt-libz.git -b libz-1.2.8 --depth=1
git clone https://github.com/curl/curl.git -b curl-7_54_1 --depth=1
export CC=gcc-4.9
export AR=gcc-ar-4.9
export RANLIB=gcc-ranlib-4.9
export CFLAGS="-m32 -I/usr/include/i386-linux-gnu"
export CPPFLAGS="-I$(pwd)/prebuilt-libz/linux-i686/include"
export LDFLAGS="-L$(pwd)/prebuilt-libz/linux-i686/lib"
export LIBS=-ldl
cd curl
./buildconf
./configure --host i686-pc-linux-gnu --with-pic --disable-shared
make
```
Get header files from include/curl   
Get libcurl.a from lib/.libs   

**BUILD LIBCURL (linux-x86_64)**   
Open "Bash on Ubuntu on Windows"   
```
git clone https://github.com/djp952/prebuilt-libz.git -b libz-1.2.8 --depth=1
git clone https://github.com/curl/curl.git -b curl-7_54_1 --depth=1
export CC=gcc-4.9
export AR=gcc-ar-4.9
export RANLIB=gcc-ranlib-4.9
export CFLAGS="-I/usr/include/x86_64-linux-gnu"
export CPPFLAGS="-I$(pwd)/prebuilt-libz/linux-x86_64/include"
export LDFLAGS="-L$(pwd)/prebuilt-libz/linux-x86_64/lib" 
export LIBS=-ldl
cd curl
./buildconf
./configure --with-pic --disable-shared
make
```
Get header files from include/curl   
Get libcurl.a from lib/.libs   
   
**BUILD LIBCURL (linux-armel)**   
Open "Bash on Ubuntu on Windows"   
```
git clone https://github.com/djp952/prebuilt-libz.git -b libz-1.2.8 --depth=1
git clone https://github.com/curl/curl.git -b curl-7_54_1 --depth=1
export CC=arm-linux-gnueabi-gcc-4.9
export AR=arm-linux-gnueabi-gcc-ar-4.9
export RANLIB=arm-linux-gnueabi-gcc-ranlib-4.9
export CPPFLAGS="-I$(pwd)/prebuilt-libz/linux-armel/include"
export LDFLAGS="-L$(pwd)/prebuilt-libz/linux-armel/lib" 
export LIBS=-ldl
cd curl
./buildconf
./configure --with-pic --host=arm-linux-gnueabi --disable-shared
make
```
Get header files from include/curl   
Get libcurl.a from lib/.libs   
   
**BUILD LIBCURL (linux-armhf)**   
Open "Bash on Ubuntu on Windows"   
```
git clone https://github.com/djp952/prebuilt-libz.git -b libz-1.2.8 --depth=1
git clone https://github.com/curl/curl.git -b curl-7_54_1 --depth=1
export CC=arm-linux-gnueabihf-gcc-4.9
export AR=arm-linux-gnueabihf-gcc-ar-4.9
export RANLIB=arm-linux-gnueabihf-gcc-ranlib-4.9
export CPPFLAGS="-I$(pwd)/prebuilt-libz/linux-armhf/include"
export LDFLAGS="-L$(pwd)/prebuilt-libz/linux-armhf/lib" 
export LIBS=-ldl
cd curl
./buildconf
./configure --with-pic --host=arm-linux-gnueabihf --disable-shared
make
```
Get header files from include/curl   
Get libcurl.a from lib/.libs   
   
**BUILD LIBCURL (linux-aarch64)**   
Open "Bash on Ubuntu on Windows"   
```
git clone https://github.com/djp952/prebuilt-libz.git -b libz-1.2.8 --depth=1
git clone https://github.com/curl/curl.git -b curl-7_54_1 --depth=1
export CC=aarch64-linux-gnu-gcc-4.9
export AR=aarch64-linux-gnu-gcc-ar-4.9
export RANLIB=aarch64-linux-gnu-gcc-ranlib-4.9
export CPPFLAGS="-I$(pwd)/prebuilt-libz/linux-aarch64/include"
export LDFLAGS="-L$(pwd)/prebuilt-libz/linux-aarch64/lib" 
export LIBS=-ldl
cd curl
./buildconf
./configure --with-pic --host=aarch64-linux-gnu --disable-shared
make
```
Get header files from include/curl   
Get libcurl.a from lib/.libs   
   
**BUILD LIBCURL (android-armeabi-v7a)**
Open "Bash on Ubuntu on Windows"   
```
git clone https://github.com/djp952/prebuilt-libz.git -b libz-1.2.8 --depth=1
git clone https://github.com/curl/curl.git -b curl-7_54_1 --depth=1
export PATH=$(pwd)/arm-linux-androideabi/bin:$PATH
export CROSS_COMPILE=arm-linux-androideabi-
export CPPFLAGS="-I$(pwd)/prebuilt-libz/android-armeabi-v7a/include"
export LDFLAGS="-L$(pwd)/prebuilt-libz/android-armeabi-v7a/lib"
export LIBS=-ldl
cd curl
./buildconf
./configure --with-pic --host=arm-linux-androideabi --target=arm-linux-androideabi --with-zlib --disable-shared
make
```
Get header files from include/curl   
Get libcurl.a from lib/.libs   
   
**BUILD LIBCURL (android-arm64-v8a)**
Open "Bash on Ubuntu on Windows"   
```
git clone https://github.com/djp952/prebuilt-libz.git -b libz-1.2.8 --depth=1
git clone https://github.com/curl/curl.git -b curl-7_54_1 --depth=1
export PATH=$(pwd)/aarch64-linux-android/bin:$PATH
export CROSS_COMPILE=aarch64-linux-android-
export CPPFLAGS="-I$(pwd)/prebuilt-libz/android-arm64-v8a/include"
export LDFLAGS="-L$(pwd)/prebuilt-libz/android-arm64-v8a/lib"
export LIBS=-ldl
cd curl
./buildconf
./configure --with-pic --host=aarch64-linux-android --target=aarch64-linux-android --with-zlib --disable-shared
make
```
Get header files from include/curl   
Get libcurl.a from lib/.libs   
   
**BUILD LIBCURL (android-x86)**
Open "Bash on Ubuntu on Windows"   
```
git clone https://github.com/djp952/prebuilt-libz.git -b libz-1.2.8 --depth=1
git clone https://github.com/curl/curl.git -b curl-7_54_1 --depth=1
export PATH=$(pwd)/i686-linux-android/bin:$PATH
export CROSS_COMPILE=i686-linux-android-
export CPPFLAGS="-I$(pwd)/prebuilt-libz/android-x86/include"
export LDFLAGS="-L$(pwd)/prebuilt-libz/android-x86/lib"
export LIBS=-ldl
cd curl
./buildconf
./configure --with-pic --host=i686-linux-android --target=i686-linux-android --with-zlib --disable-shared
make
```
Get header files from include/curl   
Get libcurl.a from lib/.libs   
   
**BUILD LIBCURL (raspbian-armhf)**   
Open "Bash on Ubuntu on Windows"   
```
git clone https://github.com/raspberrypi/tools.git raspberrypi --depth=1
git clone https://github.com/djp952/prebuilt-libz.git -b libz-1.2.8 --depth=1
git clone https://github.com/curl/curl.git -b curl-7_54_1 --depth=1
export PATH=$(pwd)/raspberrypi/arm-bcm2708/gcc-linaro-arm-linux-gnueabihf-raspbian-x64/bin:$PATH
export CC=arm-linux-gnueabihf-gcc
export AR=arm-linux-gnueabihf-gcc-ar
export RANLIB=arm-linux-gnueabihf-gcc-ranlib
export CPPFLAGS="-I$(pwd)/prebuilt-libz/raspbian-armhf/include"
export LDFLAGS="-L$(pwd)/prebuilt-libz/raspbian-armhf/lib" 
export LIBS=-ldl
cd curl
./buildconf
./configure --with-pic --host=arm-linux-gnueabihf --disable-shared
make
```
Get header files from include/curl   
Get libcurl.a from lib/.libs   
   
