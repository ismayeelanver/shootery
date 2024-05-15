[app]
# (str) Title of your application
title = Shooter2D

# (str) Package name
package.name = shooter2d

# (str) Package domain (needed for android/ios packaging)
package.domain = org.example

# (str) Source code where the main.py live
source.dir = .

# (list) Source files to include (let empty to include all the files)
source.include_exts = py,png,jpg,mp3,ogg,kv,atlas

# (list) Application requirements
# comma separated e.g. requirements = sqlite3,kivy
requirements = python3,pygame,asyncio

# (str) Target to build (android, ios, windows, macosx, linux, p4a)
target = android

# (str) Application versioning (method 1)
version = 1.0

# (str) Supported orientation (one of landscape, sensorLandscape, portrait or all)
orientation = landscape

# (list) Permissions
android.permissions = INTERNET

# (str) Package description
description = A simple 2D shooter game built with Pygame

# (str) Path to the icon of the application
icon.filename = %(source.dir)s/Graphics/icon.png

# (str) Presplash of the application
presplash.filename = %(source.dir)s/Graphics/splash.png

# (str) Presplash background color (for android)
presplash.color = #ffffff

# (bool) Indicate if the application should be fullscreen
fullscreen = 1

# (str) Extra command to pass to p4a
p4a.extra_args = --requirement=python3 --requirement=pygame --requirement=asyncio

# (list) Add custom sources for requirements
# p4a.source.include_exts =

# (str) Custom source folder for requirements
# source.include_exts =

# (str) The URL for the web application
# url = 

# (list) The list of classes that should be automatically converted to files
# (list) Override the bootstrap used by p4a
# (str) Bootstrap to use for android builds
# p4a.bootstrap = sdl2

# (str) Screen orientation
# screen.orientation = sensorLandscape

# (str) XML to include as <manifest> children in AndroidManifest.xml
# android.manifest.children =

# (str) XML to include within <manifest><application> in AndroidManifest.xml
# android.manifest.application.children =

# (str) Configuration for the initial window of your application (if you are running in windowed mode)
# window.size = (800, 800)

# (str) Extra command to pass to p4a
# p4a.extra_args =

# (str) Requirements to build the app
# p4a. requirements = kivy,openssl,hostpython3

# (str) Optional arguments to add to the p4a call
# p4a.optional_args = --no_use_setup_py

[buildozer]
# (str) Log level (0 = error only, 1 = warning, 2 = debug, 3 = info, 4 = trace)
log_level = 2

# (bool) Enable the buildozer verbose mode
verbose = 1

# (str) Command to use to run the app on the device
# run_command =

# (str) Arguments to pass to adb
# adb_args = -d

# (str) Path to the Android SDK, NDK and/or JDK
# android.sdk_path = /path/to/android-sdk
# android.ndk_path = /path/to/android-ndk
# android.ndk_api = 21
# android.sdk_api = 30
# android.build_tools = 30.0.3

# (str) Android entry point
# android.entrypoint =

# (str) Java source files to include for android
# source.java.exclude =

# (str) Include Java source files
# source.java.include =

# (str) Include Android AAR files
# android.aar.include =

# (list) List of permissions to include in the manifest
# android.permissions = INTERNET

# (str) Extra xml to include in the AndroidManifest.xml
# android.manifest_xml =

# (str) Custom source folder for assets
# source.assets =

# (str) Extra p4a args
# p4a.args =

# (str) Link against additional shared libraries
# ldlibs = -L/opt/local/lib

# (str) Source directory to store the build cache
# build_cache_dir = 

# (list) The list of Android Archs
# android.archs = arm64-v8a, armeabi-v7a, x86

# (list) Additional Java classes to be included in the application
# android.add_source = 

# (str) The paths for the prebuilt assets for android
# android.prebuilt_dir = 

# (str) The file extensions to be treated as assets
# source.include_exts = py,png,jpg,kv,atlas,mp3,ogg

# (str) Key alias for the android keystore
# android.release_keystore_alias = 

# (str) Key password for the android keystore
# android.release_keystore_passwd = 

# (str) Package signature for the android keystore
# android.release_keyalias = 

# (str) Key password for the package signature
# android.release_keypass = 

# (str) Command line options for the android build
# p4a.build.options =

# (str) Location for the compiled python modules
# p4a.android.private_storage_dir = 

# (str) Additional AAR files to be included in the application
# android.aar.include = 

# (str) The url for the Java SDK
# java.sdk_url = 

# (str) Additional arguments to pass to the buildozer commands
# buildozer.extra_args = 

# (str) Additional arguments to pass to p4a
# p4a.extra_args = 

# (str) Additional arguments to pass to adb
# adb.extra_args = 

# (str) Additional arguments to pass to the application
# app.extra_args = 

# (str) The file for the blacklist
# android.manifest_blacklist = 

# (str) The file for the whitelist
# android.manifest_whitelist = 

# (str) Extra file extensions to include for Android build
# android.include_exts = 

# (str) Path to the SSL certificates
# openssl.certificates =

# (str) Path to the Java SDK
# java.sdk_path =

# (str) Path to the Java JDK
# java.jdk_path =

# (str) Path to the Java JRE
# java.jre_path =

# (str) Path to the libstdc++.so.6 file
# stdlib.libstdcpp =

# (str) Location of the libstdc++.so.6 file
# stdlib.libstdcpp_path =

# (str) The directory containing the Android libraries
# android.libs_dir =

# (str) Path to the Android SDK
# android.sdk_path =

# (str) Path to the Android NDK
# android.ndk_path =

# (str) Path to the Android JDK
# android.jdk_path =

# (str) Path to the Android JRE
# android.jre_path =

# (str) Path to the libstdc++.so.6 file
# stdlib.libstdcpp =

# (str) The directory containing the Android libraries
# android.libs_dir =

# (str) Path to the SSL certificates
# openssl.certificates =

# (str) Path to the libstdc++.so.6 file
# stdlib.libstdcpp_path =

# (str) The directory containing the Android libraries
# android.libs_dir =

# (str) Path to the SSL certificates
# openssl.certificates =

