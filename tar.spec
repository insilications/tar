#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
%define keepstatic 1
Name     : tar
Version  : 1.34
Release  : 313
URL      : file:///aot/build/clearlinux/packages/tar/tar-v1.34.tar.gz
Source0  : file:///aot/build/clearlinux/packages/tar/tar-v1.34.tar.gz
Summary  : No detailed summary available
Group    : Development/Tools
License  : GPL-3.0 GPL-3.0+
Requires: bzip2-bin
Requires: lzop-bin
Requires: pigz-bin
Requires: xz-bin
Requires: zstd-bin
BuildRequires : acl-dev
BuildRequires : acl-staticdev
BuildRequires : attr
BuildRequires : attr-dev
BuildRequires : automake
BuildRequires : automake-dev
BuildRequires : bison
BuildRequires : bzip2-dev
BuildRequires : bzip2-staticdev
BuildRequires : clr-rpm-config
BuildRequires : gettext-bin
BuildRequires : glibc-locale
BuildRequires : glibc-staticdev
BuildRequires : lbzip2
BuildRequires : libcap
BuildRequires : libcap-dev
BuildRequires : libtool
BuildRequires : libtool-dev
BuildRequires : lz4-dev
BuildRequires : lz4-staticdev
BuildRequires : lzo-dev
BuildRequires : lzo-staticdev
BuildRequires : lzop
BuildRequires : lzop-bin
BuildRequires : m4
BuildRequires : pigz
BuildRequires : pigz-bin
BuildRequires : pkg-config-dev
BuildRequires : texinfo
BuildRequires : unzip
BuildRequires : xattr
BuildRequires : xz-bin
BuildRequires : xz-dev
BuildRequires : xz-staticdev
BuildRequires : zip
BuildRequires : zlib-dev
BuildRequires : zlib-staticdev
BuildRequires : zstd-bin
BuildRequires : zstd-dev
BuildRequires : zstd-staticdev
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}
Patch1: timestamp.patch
Patch2: blocking.patch

%description
See the end of file for copying conditions.
* Introduction
Please glance through *all* sections of this
'ABOUT-NLS' and 'INSTALL' if you are not familiar with them already.

%prep
%setup -q -n tar-clr
cd %{_builddir}/tar-clr
%patch1 -p1
%patch2 -p1

%build
unset http_proxy
unset https_proxy
unset no_proxy
export SSL_CERT_FILE=/var/cache/ca-certs/anchors/ca-certificates.crt
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1638361223
export GCC_IGNORE_WERROR=1
## altflags_pgo content
## pgo generate
export PGO_GEN="-fprofile-generate=/var/tmp/pgo -fprofile-dir=/var/tmp/pgo -fprofile-abs-path -fprofile-update=atomic -fprofile-arcs -ftest-coverage -fprofile-partial-training -fprofile-correction -freorder-functions --coverage -lgcov"
export CFLAGS_GENERATE="-Ofast --param=lto-max-streaming-parallelism=16 -march=native -mtune=native -fgraphite-identity -Wall -Wl,--as-needed -Wl,--build-id=sha1 -Wl,--enable-new-dtags -Wl,--hash-style=gnu -Wl,-O2 -Wl,-z,now,-z,relro,-z,max-page-size=0x1000,-z,separate-code -Wno-error -mprefer-vector-width=256 -falign-functions=32 -flimit-function-alignment -fasynchronous-unwind-tables -fdevirtualize-at-ltrans -floop-nest-optimize -floop-block -fno-math-errno -fno-semantic-interposition -Wl,-Bsymbolic-functions -fno-stack-protector -fno-trapping-math -ftree-loop-distribute-patterns -ftree-loop-vectorize -ftree-slp-vectorize -ftree-vectorize -fuse-ld=bfd -fuse-linker-plugin -malign-data=cacheline -feliminate-unused-debug-types -fipa-pta -flto=auto -fno-plt -mtls-dialect=gnu2 -Wl,-sort-common -Wno-error -Wp,-D_REENTRANT -pipe -ffat-lto-objects -fPIC -fomit-frame-pointer -fexceptions -static-libstdc++ -static-libgcc $PGO_GEN"
export FCFLAGS_GENERATE="-Ofast --param=lto-max-streaming-parallelism=16 -march=native -mtune=native -fgraphite-identity -Wall -Wl,--as-needed -Wl,--build-id=sha1 -Wl,--enable-new-dtags -Wl,--hash-style=gnu -Wl,-O2 -Wl,-z,now,-z,relro,-z,max-page-size=0x1000,-z,separate-code -Wno-error -mprefer-vector-width=256 -falign-functions=32 -flimit-function-alignment -fasynchronous-unwind-tables -fdevirtualize-at-ltrans -floop-nest-optimize -floop-block -fno-math-errno -fno-semantic-interposition -Wl,-Bsymbolic-functions -fno-stack-protector -fno-trapping-math -ftree-loop-distribute-patterns -ftree-loop-vectorize -ftree-slp-vectorize -ftree-vectorize -fuse-ld=bfd -fuse-linker-plugin -malign-data=cacheline -feliminate-unused-debug-types -fipa-pta -flto=auto -fno-plt -mtls-dialect=gnu2 -Wl,-sort-common -Wno-error -Wp,-D_REENTRANT -pipe -ffat-lto-objects -fPIC -fomit-frame-pointer -fexceptions -static-libstdc++ -static-libgcc $PGO_GEN"
export FFLAGS_GENERATE="-Ofast --param=lto-max-streaming-parallelism=16 -march=native -mtune=native -fgraphite-identity -Wall -Wl,--as-needed -Wl,--build-id=sha1 -Wl,--enable-new-dtags -Wl,--hash-style=gnu -Wl,-O2 -Wl,-z,now,-z,relro,-z,max-page-size=0x1000,-z,separate-code -Wno-error -mprefer-vector-width=256 -falign-functions=32 -flimit-function-alignment -fasynchronous-unwind-tables -fdevirtualize-at-ltrans -floop-nest-optimize -floop-block -fno-math-errno -fno-semantic-interposition -Wl,-Bsymbolic-functions -fno-stack-protector -fno-trapping-math -ftree-loop-distribute-patterns -ftree-loop-vectorize -ftree-slp-vectorize -ftree-vectorize -fuse-ld=bfd -fuse-linker-plugin -malign-data=cacheline -feliminate-unused-debug-types -fipa-pta -flto=auto -fno-plt -mtls-dialect=gnu2 -Wl,-sort-common -Wno-error -Wp,-D_REENTRANT -pipe -ffat-lto-objects -fPIC -fomit-frame-pointer -fexceptions -static-libstdc++ -static-libgcc $PGO_GEN"
export CXXFLAGS_GENERATE="-Ofast --param=lto-max-streaming-parallelism=16 -march=native -mtune=native -fgraphite-identity -Wall -Wl,--as-needed -Wl,--build-id=sha1 -Wl,--enable-new-dtags -Wl,--hash-style=gnu -Wl,-O2 -Wl,-z,now,-z,relro,-z,max-page-size=0x1000,-z,separate-code -Wno-error -mprefer-vector-width=256 -falign-functions=32 -flimit-function-alignment -fasynchronous-unwind-tables -fdevirtualize-at-ltrans -floop-nest-optimize -floop-block -fno-math-errno -fno-semantic-interposition -Wl,-Bsymbolic-functions -fno-stack-protector -fno-trapping-math -ftree-loop-distribute-patterns -ftree-loop-vectorize -ftree-slp-vectorize -ftree-vectorize -fuse-ld=bfd -fuse-linker-plugin -malign-data=cacheline -feliminate-unused-debug-types -fipa-pta -flto=auto -fno-plt -mtls-dialect=gnu2 -Wl,-sort-common -Wno-error -Wp,-D_REENTRANT -fvisibility-inlines-hidden -pipe -ffat-lto-objects -fPIC -fomit-frame-pointer -fexceptions -static-libstdc++ -static-libgcc $PGO_GEN"
export LDFLAGS_GENERATE="-Ofast --param=lto-max-streaming-parallelism=16 -march=native -mtune=native -fgraphite-identity -Wall -Wl,--as-needed -Wl,--build-id=sha1 -Wl,--enable-new-dtags -Wl,--hash-style=gnu -Wl,-O2 -Wl,-z,now,-z,relro,-z,max-page-size=0x1000,-z,separate-code -Wno-error -mprefer-vector-width=256 -falign-functions=32 -flimit-function-alignment -fasynchronous-unwind-tables -fdevirtualize-at-ltrans -floop-nest-optimize -floop-block -fno-math-errno -fno-semantic-interposition -Wl,-Bsymbolic-functions -fno-stack-protector -fno-trapping-math -ftree-loop-distribute-patterns -ftree-loop-vectorize -ftree-slp-vectorize -ftree-vectorize -fuse-ld=bfd -fuse-linker-plugin -malign-data=cacheline -feliminate-unused-debug-types -fipa-pta -flto=auto -fno-plt -mtls-dialect=gnu2 -Wl,-sort-common -Wno-error -Wp,-D_REENTRANT -pipe -ffat-lto-objects -fPIC -fomit-frame-pointer -fexceptions -static-libstdc++ -static-libgcc $PGO_GEN"
export LIBS_GENERATE="-lgcov"
## pgo use
## -fno-tree-vectorize: disable -ftree-vectorize thus disable -ftree-loop-vectorize and -ftree-slp-vectorize -fopt-info-vec
## -Ofast -ffast-math
## -funroll-loops maybe dangerous
## -Wl,-z,max-page-size=0x1000
## -pthread -lpthread
## -Wl,-Bsymbolic-functions
export PGO_USE="-Wmissing-profile -Wcoverage-mismatch -fprofile-use=/var/tmp/pgo -fprofile-dir=/var/tmp/pgo -fprofile-abs-path -fprofile-update=atomic -fprofile-partial-training -fprofile-correction -freorder-functions"
export CFLAGS_USE="-g3 -ggdb -Ofast --param=lto-max-streaming-parallelism=16 -march=native -mtune=native -fgraphite-identity -Wall -Wl,--as-needed -Wl,--build-id=sha1 -Wl,--enable-new-dtags -Wl,--hash-style=gnu -Wl,-O2 -Wl,-z,now,-z,relro,-z,max-page-size=0x1000,-z,separate-code -Wno-error -mprefer-vector-width=256 -falign-functions=32 -flimit-function-alignment -fasynchronous-unwind-tables -fdevirtualize-at-ltrans -floop-nest-optimize -floop-block -fno-math-errno -fno-semantic-interposition -Wl,-Bsymbolic-functions -fno-stack-protector -fno-trapping-math -ftree-loop-distribute-patterns -ftree-loop-vectorize -ftree-slp-vectorize -ftree-vectorize -fuse-ld=bfd -fuse-linker-plugin -malign-data=cacheline -feliminate-unused-debug-types -fipa-pta -flto=auto -fno-plt -mtls-dialect=gnu2 -Wl,-sort-common -Wno-error -Wp,-D_REENTRANT -pipe -ffat-lto-objects -fPIC -fomit-frame-pointer -fexceptions -static-libstdc++ -static-libgcc $PGO_USE"
export FCFLAGS_USE="-g3 -ggdb -Ofast --param=lto-max-streaming-parallelism=16 -march=native -mtune=native -fgraphite-identity -Wall -Wl,--as-needed -Wl,--build-id=sha1 -Wl,--enable-new-dtags -Wl,--hash-style=gnu -Wl,-O2 -Wl,-z,now,-z,relro,-z,max-page-size=0x1000,-z,separate-code -Wno-error -mprefer-vector-width=256 -falign-functions=32 -flimit-function-alignment -fasynchronous-unwind-tables -fdevirtualize-at-ltrans -floop-nest-optimize -floop-block -fno-math-errno -fno-semantic-interposition -Wl,-Bsymbolic-functions -fno-stack-protector -fno-trapping-math -ftree-loop-distribute-patterns -ftree-loop-vectorize -ftree-slp-vectorize -ftree-vectorize -fuse-ld=bfd -fuse-linker-plugin -malign-data=cacheline -feliminate-unused-debug-types -fipa-pta -flto=auto -fno-plt -mtls-dialect=gnu2 -Wl,-sort-common -Wno-error -Wp,-D_REENTRANT -pipe -ffat-lto-objects -fPIC -fomit-frame-pointer -fexceptions -static-libstdc++ -static-libgcc $PGO_USE"
export FFLAGS_USE="-g3 -ggdb -Ofast --param=lto-max-streaming-parallelism=16 -march=native -mtune=native -fgraphite-identity -Wall -Wl,--as-needed -Wl,--build-id=sha1 -Wl,--enable-new-dtags -Wl,--hash-style=gnu -Wl,-O2 -Wl,-z,now,-z,relro,-z,max-page-size=0x1000,-z,separate-code -Wno-error -mprefer-vector-width=256 -falign-functions=32 -flimit-function-alignment -fasynchronous-unwind-tables -fdevirtualize-at-ltrans -floop-nest-optimize -floop-block -fno-math-errno -fno-semantic-interposition -Wl,-Bsymbolic-functions -fno-stack-protector -fno-trapping-math -ftree-loop-distribute-patterns -ftree-loop-vectorize -ftree-slp-vectorize -ftree-vectorize -fuse-ld=bfd -fuse-linker-plugin -malign-data=cacheline -feliminate-unused-debug-types -fipa-pta -flto=auto -fno-plt -mtls-dialect=gnu2 -Wl,-sort-common -Wno-error -Wp,-D_REENTRANT -pipe -ffat-lto-objects -fPIC -fomit-frame-pointer -fexceptions -static-libstdc++ -static-libgcc $PGO_USE"
export CXXFLAGS_USE="-g3 -ggdb -Ofast --param=lto-max-streaming-parallelism=16 -march=native -mtune=native -fgraphite-identity -Wall -Wl,--as-needed -Wl,--build-id=sha1 -Wl,--enable-new-dtags -Wl,--hash-style=gnu -Wl,-O2 -Wl,-z,now,-z,relro,-z,max-page-size=0x1000,-z,separate-code -Wno-error -mprefer-vector-width=256 -falign-functions=32 -flimit-function-alignment -fasynchronous-unwind-tables -fdevirtualize-at-ltrans -floop-nest-optimize -floop-block -fno-math-errno -fno-semantic-interposition -Wl,-Bsymbolic-functions -fno-stack-protector -fno-trapping-math -ftree-loop-distribute-patterns -ftree-loop-vectorize -ftree-slp-vectorize -ftree-vectorize -fuse-ld=bfd -fuse-linker-plugin -malign-data=cacheline -feliminate-unused-debug-types -fipa-pta -flto=auto -fno-plt -mtls-dialect=gnu2 -Wl,-sort-common -Wno-error -Wp,-D_REENTRANT -fvisibility-inlines-hidden -pipe -ffat-lto-objects -fPIC -fomit-frame-pointer -fexceptions -static-libstdc++ -static-libgcc $PGO_USE"
export LDFLAGS_USE="-g3 -ggdb -Ofast --param=lto-max-streaming-parallelism=16 -march=native -mtune=native -fgraphite-identity -Wall -Wl,--as-needed -Wl,--build-id=sha1 -Wl,--enable-new-dtags -Wl,--hash-style=gnu -Wl,-O2 -Wl,-z,now,-z,relro,-z,max-page-size=0x1000,-z,separate-code -Wno-error -mprefer-vector-width=256 -falign-functions=32 -flimit-function-alignment -fasynchronous-unwind-tables -fdevirtualize-at-ltrans -floop-nest-optimize -floop-block -fno-math-errno -fno-semantic-interposition -Wl,-Bsymbolic-functions -fno-stack-protector -fno-trapping-math -ftree-loop-distribute-patterns -ftree-loop-vectorize -ftree-slp-vectorize -ftree-vectorize -fuse-ld=bfd -fuse-linker-plugin -malign-data=cacheline -feliminate-unused-debug-types -fipa-pta -flto=auto -fno-plt -mtls-dialect=gnu2 -Wl,-sort-common -Wno-error -Wp,-D_REENTRANT -pipe -ffat-lto-objects -fPIC -fomit-frame-pointer -fexceptions -static-libstdc++ -static-libgcc $PGO_USE"
#
export AR=/usr/bin/gcc-ar
export RANLIB=/usr/bin/gcc-ranlib
export NM=/usr/bin/gcc-nm
#
export MAKEFLAGS=%{?_smp_mflags}
#
%global _lto_cflags 1
#global _lto_cflags %{nil}
%global _disable_maintainer_mode 1
#%global _disable_maintainer_mode %{nil}
#
export CCACHE_DISABLE=true
export CCACHE_NOHASHDIR=true
export CCACHE_CPP2=true
export CCACHE_SLOPPINESS=pch_defines,time_macros,locale,file_stat_matches,file_stat_matches_ctime,include_file_ctime,include_file_mtime,modules,system_headers,clang_index_store,file_macro
#export CCACHE_SLOPPINESS=modules,include_file_mtime,include_file_ctime,time_macros,pch_defines,file_stat_matches,clang_index_store,system_headers,locale
#export CCACHE_SLOPPINESS=pch_defines,time_macros,locale,clang_index_store,file_macro
export CCACHE_DIR=/var/tmp/ccache
export CCACHE_BASEDIR=/builddir/build/BUILD
#export CCACHE_LOGFILE=/var/tmp/ccache/cache.debug
#export CCACHE_DEBUG=true
#export CCACHE_NODIRECT=true
#
export LD_LIBRARY_PATH="/usr/nvidia/lib64:/usr/nvidia/lib64/vdpau:/usr/nvidia/lib64/xorg/modules/drivers:/usr/nvidia/lib64/xorg/modules/extensions:/usr/local/cuda/lib64:/usr/lib64/haswell:/usr/lib64/haswell/pulseaudio:/usr/lib64/haswell/alsa-lib:/usr/lib64/haswell/gstreamer-1.0:/usr/lib64/haswell/pipewire-0.3:/usr/lib64/haswell/spa-0.2:/usr/lib64/dri:/usr/lib64/chromium:/usr/lib64:/usr/lib64/pulseaudio:/usr/lib64/alsa-lib:/usr/lib64/gstreamer-1.0:/usr/lib64/pipewire-0.3:/usr/lib64/spa-0.2:/usr/lib:/aot/intel/oneapi/compiler/latest/linux/compiler/lib/intel64_lin:/aot/intel/oneapi/compiler/latest/linux/lib:/aot/intel/oneapi/mkl/latest/lib/intel64:/aot/intel/oneapi/tbb/latest/lib/intel64/gcc4.8:/usr/share:/usr/lib64/wine:/usr/nvidia/lib32:/usr/nvidia/lib32/vdpau:/usr/lib32:/usr/lib32/wine"
#
export LIBRARY_PATH="/usr/nvidia/lib64:/usr/nvidia/lib64/vdpau:/usr/nvidia/lib64/xorg/modules/drivers:/usr/nvidia/lib64/xorg/modules/extensions:/usr/local/cuda/lib64:/usr/lib64/haswell:/usr/lib64/haswell/pulseaudio:/usr/lib64/haswell/alsa-lib:/usr/lib64/haswell/gstreamer-1.0:/usr/lib64/haswell/pipewire-0.3:/usr/lib64/haswell/spa-0.2:/usr/lib64/dri:/usr/lib64/chromium:/usr/lib64:/usr/lib64/pulseaudio:/usr/lib64/alsa-lib:/usr/lib64/gstreamer-1.0:/usr/lib64/pipewire-0.3:/usr/lib64/spa-0.2:/usr/lib:/aot/intel/oneapi/compiler/latest/linux/compiler/lib/intel64_lin:/aot/intel/oneapi/compiler/latest/linux/lib:/aot/intel/oneapi/mkl/latest/lib/intel64:/aot/intel/oneapi/tbb/latest/lib/intel64/gcc4.8:/usr/share:/usr/lib64/wine:/usr/nvidia/lib32:/usr/nvidia/lib32/vdpau:/usr/lib32:/usr/lib32/wine"
#
export PATH="/usr/lib64/ccache/bin:/usr/local/cuda/bin:/usr/nvidia/bin:/usr/bin/haswell:/usr/bin:/usr/sbin"
#
export CPATH="/usr/local/cuda/include"
#
export DISPLAY=:0
export __GL_SYNC_TO_VBLANK=1
export __GL_SYNC_DISPLAY_DEVICE=HDMI-0
export VDPAU_NVIDIA_SYNC_DISPLAY_DEVICE=HDMI-0
export LANG=en_US.UTF-8
export XDG_CONFIG_DIRS=/usr/share/xdg:/etc/xdg
export XDG_SEAT=seat0
export XDG_SESSION_TYPE=tty
export XDG_CURRENT_DESKTOP=KDE
export XDG_SESSION_CLASS=user
export XDG_VTNR=1
export XDG_SESSION_ID=1
export XDG_RUNTIME_DIR=/run/user/1000
export XDG_DATA_DIRS=/usr/local/share:/usr/share
export KDE_SESSION_VERSION=5
export KDE_SESSION_UID=1000
export KDE_FULL_SESSION=true
export KDE_APPLICATIONS_AS_SCOPE=1
export VDPAU_DRIVER=nvidia
export LIBVA_DRIVER_NAME=vdpau
export LIBVA_DRIVERS_PATH=/usr/lib64/dri
export GTK_RC_FILES=/etc/gtk/gtkrc
export FONTCONFIG_PATH=/usr/share/defaults/fonts
## altflags_pgo end
if [ ! -f statuspgo ]; then
echo PGO Phase 1
export CFLAGS="${CFLAGS_GENERATE}"
export CXXFLAGS="${CXXFLAGS_GENERATE}"
export FFLAGS="${FFLAGS_GENERATE}"
export FCFLAGS="${FCFLAGS_GENERATE}"
export LDFLAGS="${LDFLAGS_GENERATE}"
export LIBS="${LIBS_GENERATE}"
%configure  --disable-shared \
--enable-static \
--enable-acl \
--with-xattrs \
--with-gzip=pigz \
--with-bzip2=lbzip2 \
--disable-gcc-warnings
## make_prepend content
sd "\-lacl" "/usr/lib64/libacl.a" $(fd -uu --follow .*Makefile$) $(fd -uu --follow .*mk$)
## make_prepend end
make  %{?_smp_mflags}    V=1 VERBOSE=1

## profile_payload start
unset LD_LIBRARY_PATH
unset LIBRARY_PATH
export LD_LIBRARY_PATH="$PWD:/usr/nvidia/lib64:/usr/nvidia/lib64/vdpau:/usr/nvidia/lib64/xorg/modules/drivers:/usr/nvidia/lib64/xorg/modules/extensions:/usr/local/cuda/lib64:/usr/lib64/haswell:/usr/lib64/haswell/pulseaudio:/usr/lib64/haswell/alsa-lib:/usr/lib64/haswell/gstreamer-1.0:/usr/lib64/haswell/pipewire-0.3:/usr/lib64/haswell/spa-0.2:/usr/lib64/dri:/usr/lib64/chromium:/usr/lib64:/usr/lib64/pulseaudio:/usr/lib64/alsa-lib:/usr/lib64/gstreamer-1.0:/usr/lib64/pipewire-0.3:/usr/lib64/spa-0.2:/usr/lib:/aot/intel/oneapi/compiler/latest/linux/compiler/lib/intel64_lin:/aot/intel/oneapi/compiler/latest/linux/lib:/aot/intel/oneapi/mkl/latest/lib/intel64:/aot/intel/oneapi/tbb/latest/lib/intel64/gcc4.8:/usr/share:/usr/lib64/wine:/usr/nvidia/lib32:/usr/nvidia/lib32/vdpau:/usr/lib32:/usr/lib32/wine"
export LIBRARY_PATH="$PWD:/usr/nvidia/lib64:/usr/nvidia/lib64/vdpau:/usr/nvidia/lib64/xorg/modules/drivers:/usr/nvidia/lib64/xorg/modules/extensions:/usr/local/cuda/lib64:/usr/lib64/haswell:/usr/lib64/haswell/pulseaudio:/usr/lib64/haswell/alsa-lib:/usr/lib64/haswell/gstreamer-1.0:/usr/lib64/haswell/pipewire-0.3:/usr/lib64/haswell/spa-0.2:/usr/lib64/dri:/usr/lib64/chromium:/usr/lib64:/usr/lib64/pulseaudio:/usr/lib64/alsa-lib:/usr/lib64/gstreamer-1.0:/usr/lib64/pipewire-0.3:/usr/lib64/spa-0.2:/usr/lib:/aot/intel/oneapi/compiler/latest/linux/compiler/lib/intel64_lin:/aot/intel/oneapi/compiler/latest/linux/lib:/aot/intel/oneapi/mkl/latest/lib/intel64:/aot/intel/oneapi/tbb/latest/lib/intel64/gcc4.8:/usr/share:/usr/lib64/wine:/usr/nvidia/lib32:/usr/nvidia/lib32/vdpau:/usr/lib32:/usr/lib32/wine"
export CFLAGS="${CFLAGS_GENERATE}"
export CXXFLAGS="${CXXFLAGS_GENERATE}"
export FFLAGS="${FFLAGS_GENERATE}"
export FCFLAGS="${FCFLAGS_GENERATE}"
export LDFLAGS="${LDFLAGS_GENERATE}"
export LIBS="${LIBS_GENERATE}"
pushd src/
./tar --create --file=- "/usr/lib64/haswell"/ | lbzip2 --keep --stdout --best -n 16 -9 > teste.tar.bz2
lbzip2 -n 16 --stdout --decompress teste.tar.bz2 | ./tar -xof -
./tar --create --file=- "/usr/lib64/haswell"/ | pigz -9 -p 16 > teste2.tar.gz
pigz -dc -p 16 teste2.tar.gz | ./tar -xof -
popd
make -j1 check V=1 VERBOSE=1 || :
export LD_LIBRARY_PATH="/usr/nvidia/lib64:/usr/nvidia/lib64/vdpau:/usr/nvidia/lib64/xorg/modules/drivers:/usr/nvidia/lib64/xorg/modules/extensions:/usr/local/cuda/lib64:/usr/lib64/haswell:/usr/lib64/haswell/pulseaudio:/usr/lib64/haswell/alsa-lib:/usr/lib64/haswell/gstreamer-1.0:/usr/lib64/haswell/pipewire-0.3:/usr/lib64/haswell/spa-0.2:/usr/lib64/dri:/usr/lib64/chromium:/usr/lib64:/usr/lib64/pulseaudio:/usr/lib64/alsa-lib:/usr/lib64/gstreamer-1.0:/usr/lib64/pipewire-0.3:/usr/lib64/spa-0.2:/usr/lib:/aot/intel/oneapi/compiler/latest/linux/compiler/lib/intel64_lin:/aot/intel/oneapi/compiler/latest/linux/lib:/aot/intel/oneapi/mkl/latest/lib/intel64:/aot/intel/oneapi/tbb/latest/lib/intel64/gcc4.8:/usr/share:/usr/lib64/wine:/usr/nvidia/lib32:/usr/nvidia/lib32/vdpau:/usr/lib32:/usr/lib32/wine"
export LIBRARY_PATH="/usr/nvidia/lib64:/usr/nvidia/lib64/vdpau:/usr/nvidia/lib64/xorg/modules/drivers:/usr/nvidia/lib64/xorg/modules/extensions:/usr/local/cuda/lib64:/usr/lib64/haswell:/usr/lib64/haswell/pulseaudio:/usr/lib64/haswell/alsa-lib:/usr/lib64/haswell/gstreamer-1.0:/usr/lib64/haswell/pipewire-0.3:/usr/lib64/haswell/spa-0.2:/usr/lib64/dri:/usr/lib64/chromium:/usr/lib64:/usr/lib64/pulseaudio:/usr/lib64/alsa-lib:/usr/lib64/gstreamer-1.0:/usr/lib64/pipewire-0.3:/usr/lib64/spa-0.2:/usr/lib:/aot/intel/oneapi/compiler/latest/linux/compiler/lib/intel64_lin:/aot/intel/oneapi/compiler/latest/linux/lib:/aot/intel/oneapi/mkl/latest/lib/intel64:/aot/intel/oneapi/tbb/latest/lib/intel64/gcc4.8:/usr/share:/usr/lib64/wine:/usr/nvidia/lib32:/usr/nvidia/lib32/vdpau:/usr/lib32:/usr/lib32/wine"
## profile_payload end
make clean || :
echo USED > statuspgo
fi
if [ -f statuspgo ]; then
echo PGO Phase 2
export CFLAGS="${CFLAGS_USE}"
export CXXFLAGS="${CXXFLAGS_USE}"
export FFLAGS="${FFLAGS_USE}"
export FCFLAGS="${FCFLAGS_USE}"
export LDFLAGS="${LDFLAGS_USE}"
export LIBS="${LIBS_USE}"
%configure  --disable-shared \
--enable-static \
--enable-acl \
--with-xattrs \
--with-gzip=pigz \
--with-bzip2=lbzip2 \
--disable-gcc-warnings
## make_prepend content
sd "\-lacl" "/usr/lib64/libacl.a" $(fd -uu --follow .*Makefile$) $(fd -uu --follow .*mk$)
## make_prepend end
make  %{?_smp_mflags}    V=1 VERBOSE=1
fi


%install
export SOURCE_DATE_EPOCH=1638361223
rm -rf %{buildroot}
%make_install

%files
%defattr(-,root,root,-)
