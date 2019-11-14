## UPCOMING

## v2019_11_14_1
* `fix swift-sh brew install path, install on Xcode 9+`

## v2019_11_13_2
* `removed old android emulators up to api level 25`

## v2019_11_13_1
* `bitrise` (CLI): `1.36.0`
* `swift-sh`: `1.14.1`
* `firebase`: `7.6.2`

## `v2019_11_06_1`
* `removed deprecated cocoapods version (<1.0) related weekly update`

## `v2019_11_05_1`
* `implemented a bugfix for the recent CocoaPods specs install issue`


## `v2019_11_04_1`
* `flutter`: `v1.9.1+hotfix.6`

## `v2019_10_24_1`
* `remove bundletools from system report`

## `v2019_10_10_1`
* `changed ruby versions to the ones rbenv can actually install`

## `v2019_10_09_1`
* `bitrise` (CLI): `1.35.0`

## `v2019_10_04_01`
* `ruby-versions`: `updated default to latest stable, updated minor versions, and removed deprecated versions`

## `v2019_10_01_1`
* `java-tools`: `Ant version back to latest`

## `v2019_09_26_1`
* `java-tools`: `Ant version fixed @1.9`

## `v2019_09_20_1`
* `flutter`: `v1.9.1+hotfix.2`
* `Android NDK`: `r20`

## `v2019_09_11_2`
* `bitrise` (CLI): `1.34.0`

## `v2019_09_11_1`
* Preinstalled android packages for buidling against Android 10:
  * `build-tools-29.0.0`,`build-tools-29.0.1`, `build-tools-29.0.2`
  * `platforms;android-29`
  * `system-images;android-29;google_apis;x86`

## `v2019_08_21_1`
* `bitrise` (CLI): `1.33.0`

## `v2019_06_12_1`
* `bitrise` (CLI): `1.31.0`

## `v2019_05_15_1`
* `bitrise` (CLI): `1.30.0`

## `v2019_05_07_1`

* New stack types will have rbenv installed ruby with the following versions:
  * 2.6.3
  * 2.5.5
  * 2.4.6
  * 2.3.8
  * 2.2.10

## `v2019_04_18_1`
* `Java`: Switched to AdoptOpenJDK distributed Java 8

## `v2019_04_10_1`
* `bitrise` (CLI): `1.29.0`

## `v2019_04_05_1`
* `flutter`: installed

## `v2019_04_03_1`
* `ngrok link`: installed

## `v2019_04_02_1`
* `bitrise-bridge`: removed

## `v2019_03_20_1`
* `Playbook`: Removed authorized_keys

## `v2019_03_13_1`
* `bitrise` (CLI): `1.28.0`

## `v2019_03_11_1`
* `git` default user changed to "J. Doe (https://devcenter.bitrise.io/builds/setting-your-git-credentials-on-build-machines/)"

## `v2019_02_28_1`
* Install Android tools from brew instead of direct link

## `v2019_02_20_1`
* `bitrise` (CLI): `1.27.1`

## `v2019_02_19_1`
* Playbook: Upgraded `NodeJS` from 8.x to 10.x as it is the Active LTS now

## `v2019_02_13_2`
* `bitrise` (CLI): `1.27.0`

## `v2019_02_13_1`
* `git` default user changed to "J. Doe (https://www.git-tower.com/learn/git/faq/change-author-name-email)" and default email to "please-set-your-email@bitrise.io"

## `v2019_01_09_1`
* `bitrise` (CLI): `1.26.0`

## `v2018_12_13_1`
* Add `$ANDROID_HOME/tools/bin` to $PATH as well because it was missing

## `v2018_12_12_1`
* `bitrise` (CLI): `1.25.0`

## `v2018_12_05_1`
* Playbook for installing Android tools on plain Xcode stacks

## `v2018_11_28_1`

* New stack types will have rbenv installed ruby with the following versions:
  * 2.5.3
  * 2.4.5
  * 2.3.8
  * 2.2.10

## `v2018_11_14_2`

* New fix for Ruby and Rubygems paths

## `v2018_11_14_1`

* `bitrise` (CLI): `1.24.0`

## `v2018_11_06_1`

* Removed ulimit directive from bashrc, rely only on the plist configuration
* Fix Ruby and Rubygems paths

## `v2018_10_10_1`

* `bitrise` (CLI): `1.23.0`

## `v2018_09_21_1`

* Incrased Open File Descriptors to 200.000

## `v2018_09_12_1`

* `bitrise` (CLI): `1.22.0`

## `v2018_08_16_1`

* `bitrise` (CLI): `1.21.0`

## `v2018_08_02_1`

* `node` LTS version will be used in the future (currently 8.x)

## `v2018_07_25_1`

* `bitrise` (CLI): `1.20.0`

## `v2018_07_12_1`

* `bitrise` (CLI): `1.19.0`

## `v2018_06_28_1`

* `bitrise` (CLI): `1.18.1`

## `v2018_06_14_1`

* `bitrise` (CLI): `1.17.0`
*
## `v2018_05_16_1`

* `bitrise` (CLI): `1.16.1`

## `v2018_05_09_1`

* `bitrise` (CLI): `1.16.0`

## `v2018_04_12_1`

* Visual Studio for Mac only:
  * `Android NDK` was updated to `r15c`

## `v2018_04_11_1`

* `bitrise` (CLI): `1.15.0`

## `v2018_04_06_1`

* Visual Studio for Mac only:
  * `Java`: need to stick to Java 8 because Android's `sdkmanager` does not support neither Java 9 nor Java 10
  * all Android tool installs have been modified to use `sdkmanager`

## `v2018_03_13_1`

* `bitrise` (CLI): `1.14.0`

## `v2018_03_06_1`

* `screen` now updated from brew

## `v2018_02_13_1`

* `bitrise` (CLI): `1.13.0`

## `v2018_01_11_1`

* `bitrise` (CLI): `1.12.0`

## `v2018_01_04_1`

* `gem install bundler` removed because `bundler` comes preinstalled with rubygems

## `v2017_12_13_1`

* `bitrise` (CLI): `1.11.0`

## `v2017_11_14_1`

* `bitrise` (CLI): `1.10.1`

## `v2017_11_09_5`

* revert Java hacking

## `v2017_11_09_4`

* fix homebrew privilege issue

## `v2017_11_09_3`

* fix ansible privilege issue

## `v2017_11_09_2`

* fix ansible indentation error

## `v2017_11_09_1`

* downgrade to java 8 on VS 4 Mac stacks because of sdkmanager issue

## `v2017_10_10_1`

* `bitrise` (CLI): `1.10.0`

## `v2017_09_27_1`

* `jce-unlimited-strength-policy` cask removed
    * Java 9 can set this from code: https://stackoverflow.com/a/42163925
    * https://github.com/bitrise-io/osx-box-bootstrap/issues/55

## `v2017_09_18_1`

* Removed unused box-info.json

## `v2017_09_13_1`

* `bitrise` (CLI): `1.9.0`

## `v2017_08_30_1`

* `jce-unlimited-strength-policy` cask preinstalled
    * PR https://github.com/bitrise-io/osx-box-bootstrap/pull/50

## `v2017_08_08_1`

* `bitrise` (CLI): `1.8.0`


## `v2017_07_11_1`

* `bitrise` (CLI): `1.7.0`


## `v2017_06_13_1`

* `bitrise` (CLI): `1.6.2`


## `v2017_05_11_1`

* `bitrise` (CLI): `1.6.1`


## `v2017_05_02_1`

* Xamarin Only: .Net Core __removed__, no longer preinstalled. Please use the new `install-dotnetcore` step instead.
    * Thanks @stefandevo for the changes!
    * TL;DR; installation of .Net Core right now is still a bit "beta", we'll consider pre-installing .Net Core
      in the future again once it lands in `brew`. Until that it's way more flexible to use a Step
      instead, which can be updated any time, instead of sticking to a preinstalled version
      which is hard & slow to change.
    * Related discussion: https://github.com/bitrise-io/osx-box-bootstrap/pull/44


## `v2017_04_25_1`

* Xamarin Only: .Net Core preinstalled
    * Thanks @stefandevo for the PR https://github.com/bitrise-io/osx-box-bootstrap/pull/41


## `v2017_04_12_1`

* `bitrise` (CLI): `1.5.6`


## `v2017_03_14_1`

* `bitrise` (CLI): `1.5.5`


## `v2017_02_15_1`

* `bitrise` (CLI): `1.5.4`


## `v2017_01_12_1`

* Xamarin only: make sure that a default `debug.keystore` is available in the system


## `v2017_01_11_1`

* `bitrise` (CLI): `1.5.2`


## `v2017_01_05_1`

* Using `homebrew/versions/ruby23` for now, instead of the latest `ruby`,
  as pretty much every popular Ruby based tool have issues with Ruby 2.4 right now.
* Preinstalled `ionic` and `cordova` npm (CLI) packages


## `v2016_12_22_1`

* Disabled APSD process, due to high CPU consumption in macOS 10.12


## `v2016_12_15_1`

* `bitrise` (CLI): `1.5.1`
* Xamarin only: preinstalled `build-tools-25.0.2` android package


## `v2016_12_13_1`

* Xamarin only: `extra-android-support` is no longer available, removed
* minor system report improvements


## `v2016_11_23_1`

* Xamarin only: preinstalled `build-tools-25.0.1` android package


## `v2016_11_17_1`

* `MATCH_KEYCHAIN_PASSWORD` env var defined, to fix the `fastlane` macOS Sierra keychain handling issue (https://github.com/fastlane/fastlane/issues/6866)
* Xamarin only: removed `sys-img-armeabi-v7a-android-23`, the package is no longer available in `android update sdk`
* Xamarin only: `ANDROID_NDK_HOME` env var is now defined


## `v2016_11_10_1`

* `bitrise` (CLI): `1.4.5`


## `v2016_11_09_1`

* `bitrise` (CLI): `1.4.4`
* `cmd-bridge`: `0.9.5`
* `bitrise-bridge`: `0.9.11`
* Xamarin only: generate a debug keystore if that's missing


## `v2016_11_02_1`

* Xamarin only: `/Library/Frameworks/Mono.framework/Versions/Current/Commands` added to `PATH`


## `v2016_10_27_1`

* `xctool` removed - `brew install xctool` fails on MacOS Sierra


## `v2016_10_24_1`

* `bitrise` (CLI): `1.4.3`


## `v2016_10_20_1`

* Xamarin specific: new preinstalled packages: `android-25` & `build-tools-25.0.0`


## `v2016_10_14_1`

* `bitrise` (CLI): `1.4.2`


## `v2016_10_12_1`

* `bitrise` (CLI): `1.4.1`


## `v2016_10_04_1`

* Install `bundler` for system Ruby
* `build-tools-24.0.3` added to the Xamarin stack


## `v2016_09_14_1`

* `bitrise` (CLI): `1.4.0`


## `v2016_09_09_1`

* `bitrise-bridge`: `0.9.10`


## `v2016_08_18_1`

* `bitrise-bridge`: `0.9.9`


## `v2016_08_10_1`

* `bitrise` (CLI): `1.3.7`


## `v2016_07_21_1`

* Xamarin specific: added new preinstalled Android packages: `build-tools-24.0.1` & `sys-img-armeabi-v7a-android-24`
* preinstalled `imagemagick` - thanks to [@samdods' PR](https://github.com/bitrise-io/osx-box-bootstrap/pull/13)!
* preinstalled `ghostscript` - thanks to [@samdods' PR](https://github.com/bitrise-io/osx-box-bootstrap/pull/13)!


## `v2016_07_14_1`

* `bitrise` (CLI): `1.3.6`


## `2016_07_02_1`

* `git config --global user.email` and `git config --global user.name`, for easier tag publishing (or other git push operation)
* [git-lfs](https://git-lfs.github.com/) pre-installed


## `2016_06_18_1`

* `android-24` is no longer preview - package names were changed


## `2016_06_15_3`

* `xcode-version-map-files-playbook` / `DEPRECATED-create-xcode-version-mapping` removed. This was deprecated
  for a long time now, and it had no purpose on the new Stacks / recommended environments, where only one Xcode
  is available, at it's canonical location (in `/Applications/`)


## `2016_06_15_2`

* `ruby` : switched back from our pinned Ruby 2.2.4 to the latest `brew` installed ruby version.
  CocoaPods 1.x should properly work with the new `ruby` version now.


## `2016_06_15_1`

* `wine` removed. We really wanted to keep it around, but so far we had more issues with `wine` than we had with any other tool..
  We decided to remove it for now as it breaks the install/provision process - if the new Xcode 8 (beta) is installed on the system
  `wine` fails to install.


## `2016_06_11_1`

* `bitrise` (CLI): `1.3.5`


## `2016_05_14_1`

* `bitrise` (CLI): `1.3.4`


## `2016_04_27_1`

* `bitrise` (CLI) : `1.3.3`


## `2016_04_26_1`

* Bit of reorganization: after `bitrise run provision-vm` you now have to run `bitrise run perform-weekly-cache-update`,
  to not to duplicate tasks/scripts between the initial setup and the weekly cache updates.
* `bitrise` (CLI) : `1.3.2`
* `bitrise-bridge` : `0.9.8`
* Cleanup: make sure that `~/Library/Developer/Xcode/DerivedData` is empty before saving the virtual machine image


## `2016_04_04_1`

* `Build tool 23.0.3` added to the Xamarin stack
* `NUnit 2.6.4` added to the stack

## `2016_03_17_1`

* `java` is now pre-installed - thanks @izhilenkov! 🙌
* `NUnit` updated to `3.2`

## `2016_02_24_2`

* `wine`: http://www.freedesktop.org/ is alive again, `wine` install went through.

## `2016_02_24_1`

* `wine` temporarily removed from this version. There's an ongoing issue with
  one of its dependency which downloads from http://www.freedesktop.org/ - the
  site is down for more than 5 hours now.

## `2016_02_10_1`

* `wine` and `xquartz` are pre-installed now

## `2016_01_28_1`

* `carthage` is now pre-installed


## `2016_01_18_1`

* Updated `ansible` playbooks, for Ansible 2.0
* Xcode path can (and should) be specified.


## `2016_01_13_1`

* `tree` is now pre-installed
* The current Revision ID is now available in the `bitrise_profile` (loaded automatically,
  through `.bashrc`),
  and can be accessed with the Environment Variable `BITRISE_OSX_STACK_REV_ID`.
