%global package_speccommit b4c71dd4d02eae0e6345d47ae189570d78964970
%global usver 9.9.4
%global xsver 63
%global xsrel %{xsver}%{?xscount}%{?xshash}

#
# Red Hat BIND package .spec file
#

#%%global PATCHVER P2
#%%global PREVER rc2
#%%global VERSION %{version}%{PREVER}
%global VERSION %{version}
#%%global VERSION %{version}-%{PATCHVER}

%{?!SDB:       %global SDB       0}
%{?!test:      %global test      0}
%{?!bind_uid:  %global bind_uid  25}
%{?!bind_gid:  %global bind_gid  25}
%{?!GSSTSIG:   %global GSSTSIG   1}
%{?!PKCS11:    %global PKCS11    1}
%{?!DEVEL:     %global DEVEL     1}
%global        bind_dir          /var/named
%global        chroot_prefix     %{bind_dir}/chroot
%if %{SDB}
%global        chroot_sdb_prefix %{bind_dir}/chroot_sdb
%endif
#
Summary:  The Berkeley Internet Name Domain (BIND) DNS (Domain Name System) server
Name:     bind
License:  ISC
Version:  9.9.4
Release: %{?xsrel}%{?dist}
Epoch: 32
Url:      http://www.isc.org/products/BIND/
Buildroot:%{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
Group:    System Environment/Daemons
#
Source0: bind-9.9.4.tar.gz
Source1: named.sysconfig
Source3: named.logrotate
Source7: bind-9.3.1rc1-sdb_tools-Makefile.in
Source8: dnszone.schema
Source12: README.sdb_pgsql
Source25: named.conf.sample
Source28: config-15.tar.bz2
# Up-to-date bind.keys from upstream
# Fetch a new one from page https://www.isc.org/bind-keys
Source29: bind.keys
Source30: ldap2zone.c
Source31: ldap2zone.1
Source32: named-sdb.8
Source33: zonetodb.1
Source34: zone2sqlite.1
Source35: bind.tmpfiles.d
Source36: trusted-key.key
Source37: named.service
Source38: named-chroot.service
Source39: named-sdb.service
Source40: named-sdb-chroot.service
Source41: setup-named-chroot.sh
Source42: generate-rndc-key.sh
Source43: named.rwtab
Source44: named-chroot-setup.service
Source45: named-sdb-chroot-setup.service
Source46: named-setup-rndc.service
Source47: named-pkcs11.service
# added due to GeoIP functionality tests
# patch tool does not support binary patches
Source48: geoip-testing-data.tar.xz

# Common patches
Patch5:  bind-nonexec.patch
Patch10: bind-9.5-PIE.patch
Patch16: bind-9.3.2-redhat_doc.patch
Patch72: bind-9.5-dlz-64bit.patch
Patch87: bind-9.5-parallel-build.patch
Patch101:bind-96-old-api.patch
Patch102:bind-95-rh452060.patch
Patch106:bind93-rh490837.patch
Patch109:bind97-rh478718.patch
Patch110:bind97-rh570851.patch
Patch111:bind97-exportlib.patch
Patch112:bind97-rh645544.patch
Patch119:bind97-rh693982.patch
Patch123:bind98-rh735103.patch
Patch124:bind93-rh726120.patch
# FIXME: This disables dlzexternal, which I will enable later again
# Make tests on all architectures and disable it
Patch127:bind99-forward.patch
Patch130:bind-9.9.1-P2-dlz-libdb.patch
Patch131:bind-9.9.1-P2-multlib-conflict.patch
Patch133:bind99-rh640538.patch
Patch134:bind97-rh669163.patch
Patch137:bind99-rrl.patch
# Install dns/update.h header for bind-dyndb-ldap plugin
Patch138:bind-9.9.3-include-update-h.patch
Patch139:bind99-ISC-Bugs-34738.patch
Patch140:bind99-ISC-Bugs-34870-v3.patch
Patch141:bind99-ISC-Bugs-35073.patch
Patch142:bind99-ISC-Bugs-35080.patch
Patch143:bind99-CVE-2014-0591.patch
Patch144:bind99-rh1067424.patch
Patch145:bind99-rh1072379.patch
Patch146:bind99-rh1098959.patch
Patch147:bind99-CVE-2014-8500.patch
Patch148:bind99-CVE-2015-1349.patch
Patch149:bind99-rh1215687-limits.patch
Patch154:bind99-rh1215164.patch
Patch155:bind99-rh1214827.patch
Patch156:bind99-CVE-2015-4620.patch
Patch157:bind99-CVE-2015-5477.patch
Patch158:bind-99-socket-maxevents.patch
Patch159:bind99-CVE-2015-5722.patch
Patch160:bind99-CVE-2015-8000.patch
Patch161:bind99-CVE-2015-8704.patch
Patch162:bind99-CVE-2016-1285-CVE-2016-1286.patch
Patch163:bind99-rh1291185.patch
Patch164:bind99-rh1259514.patch
Patch165:bind99-rh1306610.patch
Patch166:bind99-rh1220594-geoip.patch
Patch167:bind99-automatic-interface-scanning-rh1294506.patch
# commit 51bcc28543ce205f7af238ef2f3889ef020a0961 ISC 4467
patch168:bind99-CVE-2016-2776.patch
# commit bbb7c613b3e41495db627909660334695b48e60b ISC 4489
patch169:bind99-CVE-2016-8864.patch
# commit d372472f604d45f85b3bbae5d6f523fb561a8823 ISC 4508
patch170:bind99-CVE-2016-9131.patch
# commit a14b7f0187315767a1fa855f116fe937a7b402e3 ISC 4510
patch171:bind99-CVE-2016-9147.patch
# commit 69cb8ebf157183d9c36a9813f945348dd81b521f ISC 4517
Patch172:bind99-CVE-2016-9444.patch
# commit 2c74ad28efe5710ad04562c6f9902bc48d3be0ed ISC 4530
Patch173:bind99-rt43779.patch
# commit 062b04898be720ed0855efc192847fcbc667b3e1 ISC 4406
Patch174:bind99-CVE-2016-2775.patch
# ISC 4557
Patch175:bind99-CVE-2017-3135.patch
# ISC 4558
Patch176:bind99-rt44318.patch
# commit c550e75ade4ceb4ece96f660292799519a5c3183 ISC 4567
Patch177:bind99-rh1392362.patch
# commit 1f3ac11cb4ecfab52f517ebf78493b0f05318be2
Patch178:bind99-coverity-fixes2.patch
# ISC 4575
Patch179:bind99-CVE-2017-3136.patch
# ISC 4578
Patch180:bind99-CVE-2017-3137.patch
# commit 5e746ab61ed8158f784b86111fef95581a08b7dd ISC 3905
Patch181:bind99-rh1416304.patch
# ISC 4643
Patch182: bind99-CVE-2017-3142+3143.patch
# commit e3894cd3a92be79a64072835008ec589b17c601a
Patch183: bind99-rh1472862.patch
# commit 2fc1b8102d4bf02162012c27ab95e98a7438bd8f ISC 4647
Patch184: bind99-rh1476013.patch
# commit 51aed1827453f40ee56b165d45c5d58d96838d94
Patch185: bind99-rh1470637-tests.patch
# commit 51b00c6c783ccf5dca86119ff8f4f8b994298ca4 ISC 4712
Patch186: bind99-rh1470637.patch
# commit 6a3fa181d1253db5191139e20231512eebaddeeb ISC 3745
Patch187: bind99-rh1464850.patch
# commit 871f3c8beeb2134b17414ec167b90a57adb8e122 ISC 3980
Patch188: bind99-rh1464850-2.patch
# commit 4eb998928b9aef0ceda42d7529980d658138698a ISC 3525
Patch189: bind99-rh1501531.patch
# ISC 4858
Patch190: bind99-CVE-2017-3145.patch
Patch191: bind99-CVE-2018-5740.patch

# Native PKCS#11 functionality from 9.10
Patch150:bind-9.9-allow_external_dnskey.patch
Patch151:bind-9.9-native-pkcs11.patch
Patch152:bind-9.9-dist-native-pkcs11.patch
Patch153:bind99-coverity-fixes.patch

# SDB patches
Patch11: bind-9.3.2b2-sdbsrc.patch
Patch12: bind-9.5-sdb.patch
Patch62: bind-9.5-sdb-sqlite-bld.patch

# needs inpection
Patch17: bind-9.3.2b1-fix_sdb_ldap.patch
Patch104: bind99-dyndb.patch

# IDN paches
Patch73: bind-9.5-libidn.patch
Patch83: bind-9.5-libidn2.patch
Patch85: bind-9.5-libidn3.patch
Patch94: bind95-rh461409.patch
Patch135:bind99-libidn4.patch

Patch300: Remove-openssl-version-check.patch
Patch301: Fix-openssldh-build-error-1.patch
Patch302: Fix-openssldh-build-error-2.patch
Patch303: Fix-openssldsa-build-error.patch
Patch304: Fix-pensslecdsa-pensslrsa-build-error.patch
Patch305: Remove-support-for-obsoleted-and-insecure-DSA-and-DS-1.patch
Patch306: Remove-support-for-obsoleted-and-insecure-DSA-and-DS-2.patch

#
Requires(preun):  systemd
Requires(postun): systemd
Requires:       coreutils
Requires:       systemd-units
Requires(post): grep, systemd
Requires(pre):  shadow-utils
Requires:       bind-libs = %{epoch}:%{version}-%{release}
Obsoletes:      bind-config < 30:9.3.2-34.fc6
Provides:       bind-config = 30:9.3.2-34.fc6
Obsoletes:      caching-nameserver < 31:9.4.1-7.fc8
Provides:       caching-nameserver = 31:9.4.1-7.fc8
Obsoletes:      dnssec-conf < 1.27-2
Provides:       dnssec-conf = 1.27-1
BuildRequires:  openssl-devel, libtool, autoconf, pkgconfig, libcap-devel
BuildRequires:  libidn-devel, libxml2-devel, GeoIP-devel
BuildRequires:  systemd-units
%if %{SDB}
BuildRequires:  openldap-devel, sqlite-devel
BuildRequires:  libdb-devel
%endif
%if %{test}
BuildRequires:  net-tools
%endif
%if %{GSSTSIG}
BuildRequires:  krb5-devel
%endif
# Needed to regenerate dig.1 manpage
BuildRequires: docbook-style-xsl, libxslt

%description
BIND (Berkeley Internet Name Domain) is an implementation of the DNS
(Domain Name System) protocols. BIND includes a DNS server (named),
which resolves host names to IP addresses; a resolver library
(routines for applications to use when interfacing with DNS); and
tools for verifying that the DNS server is operating properly.

%if %{PKCS11}
%package pkcs11
Summary: Bind with native PKCS#11 functionality for crypto
Group:   System Environment/Daemons
Requires: bind = %{epoch}:%{version}-%{release}
Requires: bind-libs = %{epoch}:%{version}-%{release}
Requires: bind-pkcs11-libs = %{epoch}:%{version}-%{release}

%description pkcs11
This is a version of BIND server built with native PKCS#11 functionality.
It is important to have SoftHSM v2+ installed and some token initialized.
For other supported HSM modules please check the BIND documentation.
This version of BIND binary is supported only in setup with the IPA server.

%package pkcs11-utils
Summary: Bind tools with native PKCS#11 for using DNSSEC
Group:   System Environment/Daemons
Requires: bind-pkcs11-libs = %{epoch}:%{version}-%{release}

%description pkcs11-utils
This is a set of PKCS#11 utilities that when used together create rsa
keys in a PKCS11 keystore. Also utilities for working with DNSSEC
compiled with native PKCS#11 functionality are included.

%package pkcs11-libs
Summary: Bind libraries compiled with native PKCS#11
Group:   System Environment/Daemons
Requires: bind-license = %{epoch}:%{version}-%{release}
Requires: bind-libs = %{epoch}:%{version}-%{release}

%description pkcs11-libs
This is a set of BIND libraries (dns, isc) compiled with native PKCS#11
functionality.

%package pkcs11-devel
Summary: Development files for Bind libraries compiled with native PKCS#11
Group:   System Environment/Daemons
Requires: bind-pkcs11-libs = %{epoch}:%{version}-%{release}

%description pkcs11-devel
This a set of development files for BIND libraries (dns, isc) compiled
with native PKCS#11 functionality.
%endif

%if %{SDB}
%package sdb
Summary: BIND server with database backends and DLZ support
Group:   System Environment/Daemons
Requires: bind
Requires: bind-libs = %{epoch}:%{version}-%{release}
Requires: systemd-units

%description sdb
BIND (Berkeley Internet Name Domain) is an implementation of the DNS
(Domain Name System) protocols. BIND includes a DNS server (named-sdb)
which has compiled-in SDB (Simplified Database Backend) which includes
support for using alternative Zone Databases stored in an LDAP server
(ldapdb), a postgreSQL database (pgsqldb), an sqlite database (sqlitedb),
or in the filesystem (dirdb), in addition to the standard in-memory RBT
(Red Black Tree) zone database. It also includes support for DLZ
(Dynamic Loadable Zones)
%endif

%package libs-lite
Summary:  Libraries for working with the DNS protocol
Group:    Applications/System
Obsoletes:bind-libbind-devel < 31:9.3.3-4.fc7
Provides: bind-libbind-devel = 31:9.3.3-4.fc7
Requires: bind-license = %{epoch}:%{version}-%{release}

%description libs-lite
Contains lite version of BIND suite libraries which are used by various
programs to work with DNS protocol.

%package libs
Summary: Libraries used by the BIND DNS packages
Group:    Applications/System
Requires: bind-license = %{epoch}:%{version}-%{release}

%description libs
Contains heavyweight version of BIND suite libraries used by both named DNS
server and utilities in bind-utils package.

%package license
Summary:  License of the BIND DNS suite
Group:    Applications/System
BuildArch:noarch

%description license
Contains license of the BIND DNS suite.

%package utils
Summary: Utilities for querying DNS name servers
Group:   Applications/System
Requires: bind-libs = %{epoch}:%{version}-%{release}

%description utils
Bind-utils contains a collection of utilities for querying DNS (Domain
Name System) name servers to find out information about Internet
hosts. These tools will provide you with the IP addresses for given
host names, as well as other information about registered domains and
network addresses.

You should install bind-utils if you need to get information from DNS name
servers.

%if %{DEVEL}
%package devel
Summary:  Header files and libraries needed for BIND DNS development
Group:    Development/Libraries
Obsoletes:bind-libbind-devel < 31:9.3.3-4.fc7
Provides: bind-libbind-devel = 31:9.3.3-4.fc7
Requires: bind-libs = %{epoch}:%{version}-%{release}

%description devel
The bind-devel package contains full version of the header files and libraries
required for development with ISC BIND 9
%endif

%package lite-devel
Summary:  Lite version of header files and libraries needed for BIND DNS development
Group:    Development/Libraries
Requires: bind-libs-lite = %{epoch}:%{version}-%{release}

%description lite-devel
The bind-lite-devel package contains lite version of the header
files and libraries required for development with ISC BIND 9

%package chroot
Summary:        A chroot runtime environment for the ISC BIND DNS server, named(8)
Group:          System Environment/Daemons
Prefix:         %{chroot_prefix}
Requires(post): grep
Requires(preun):grep
Requires:       bind = %{epoch}:%{version}-%{release}
Requires:       systemd-units

%description chroot
This package contains a tree of files which can be used as a
chroot(2) jail for the named(8) program from the BIND package.
Based on the code from Jan "Yenya" Kasprzak <kas@fi.muni.cz>

%if %{SDB}
%package sdb-chroot
Summary:        A chroot runtime environment for the ISC BIND DNS server, named-sdb(8)
Group:          System Environment/Daemons
Prefix:         %{chroot_prefix}
Requires:       bind-sdb
Requires:       systemd-units

%description sdb-chroot
This package contains a tree of files which can be used as a
chroot(2) jail for the named-sdb(8) program from the BIND package.
Based on the code from Jan "Yenya" Kasprzak <kas@fi.muni.cz>
%endif


%prep
%setup -q -n %{name}-%{VERSION}

# Common patches
%patch5 -p1 -b .nonexec
%patch10 -p1 -b .PIE
%patch16 -p1 -b .redhat_doc
%ifnarch alpha ia64
%patch72 -p1 -b .64bit
%endif
%patch73 -p1 -b .libidn
%patch83 -p1 -b .libidn2
%patch85 -p1 -b .libidn3
%patch87 -p1 -b .parallel
%patch94 -p1 -b .rh461409

%patch102 -p1 -b .rh452060
%patch106 -p0 -b .rh490837
%patch109 -p1 -b .rh478718
%patch110 -p1 -b .rh570851
%patch111 -p1 -b .exportlib
%patch112 -p1 -b .rh645544
%patch119 -p1 -b .rh693982
%patch123 -p1 -b .rh735103
%patch124 -p1 -b .rh726120
%patch127 -p1 -b .forward
%patch130 -p1 -b .libdb
%patch131 -p1 -b .multlib-conflict
%patch137 -p1 -b .rrl
%patch138 -p1 -b .update
%patch139 -p1 -b .journal
%patch140 -p1 -b .send_buffers
%patch141 -p1 -b .leak_35073
%patch142 -p1 -b .rbt_crash
%patch143 -p1 -b .CVE-2014-059
%patch144 -p1 -b .rh1067424
%patch145 -p1 -b .rh1072379
%patch146 -p1 -b .rh1098959
%patch147 -p1 -b .CVE-2014-8500
%patch148 -p1 -b .CVE-2015-1349
%patch149 -p1 -b .rh1215687-limits

%patch150 -p1 -b .external_key
%patch151 -p1 -b .native_pkcs11
# http://cov01.lab.eng.brq.redhat.com/covscanhub/waiving/9377/
%patch153 -p1 -b .coverity_9377
%patch154 -p1 -b .rh1215164
%patch155 -p1 -b .nsupdate_realm
%patch156 -p1 -b .CVE-2015-4620
%patch157 -p1 -b .CVE-2015-5477
%patch158 -p1 -b .sock-maxevents
%patch159 -p1 -b .CVE-2015-5722
%patch160 -p1 -b .CVE-2015-8000
%patch161 -p1 -b .CVE-2015-8704
%patch162 -p1 -b .CVE-2016-1285-CVE-2016-1286
%patch163 -p1 -b .rh1291185
%patch164 -p1 -b .rh1259514
%patch165 -p1 -b .rh1306610-caa
%patch104 -p1 -b .dyndb

# GeoIP support
%patch166 -p1 -b .rh1220594-geoip
# extract the binary testing data
tar -xf %{SOURCE48} -C bin/tests/system/geoip/data

%patch167 -p1 -b .rh1294506
%patch168 -p1 -b .CVE-2016-2776
%patch169 -p1 -b .CVE-2016-8864
%patch170 -p1 -b .CVE-2016-9131
%patch171 -p1 -b .CVE-2016-9147
%patch172 -p1 -b .CVE-2016-9444
%patch173 -p1 -b .rt43779
%patch174 -p1 -b .CVE-2016-2775
%patch175 -p1 -b .CVE-2017-3135
%patch176 -p1 -b .rt44318
%patch177 -p1 -b .rh1392362
%patch178 -p1 -b .coverity2
%patch179 -p1 -b .CVE-2017-3136
%patch180 -p1 -b .CVE-2017-3137
%patch181 -p1 -b .rh1416304
%patch182 -p1 -b .CVE-2017-3142+3143
%patch183 -p1 -b .rh1472862
%patch184 -p1 -b .rh1476013
%patch185 -p1 -b .rh1470637-tests
%patch186 -p1 -b .rh1470637
%patch187 -p1 -b .rh1464850
%patch188 -p1 -b .rh1464850
%patch189 -p1 -b .rh1501531
%patch190 -p1 -b .CVE-2017-3145
%patch191 -p1 -b .CVE-2018-5740

# Override upstream builtin keys
cp -fp %{SOURCE29} bind.keys

%if %{PKCS11}
cp -r bin/named{,-pkcs11}
cp -r bin/dnssec{,-pkcs11}
cp -r lib/isc{,-pkcs11}
cp -r lib/dns{,-pkcs11}
cp -r lib/export/isc{,-pkcs11}
cp -r lib/export/dns{,-pkcs11}
%patch152 -p1 -b .dist_pkcs11
%endif

%if %{SDB}
%patch101 -p1 -b .old-api
mkdir bin/named-sdb
cp -r bin/named/* bin/named-sdb
%patch11 -p1 -b .sdbsrc
# SDB ldap
cp -fp contrib/sdb/ldap/ldapdb.[ch] bin/named-sdb
# SDB postgreSQL
cp -fp contrib/sdb/pgsql/pgsqldb.[ch] bin/named-sdb
# SDB sqlite
cp -fp contrib/sdb/sqlite/sqlitedb.[ch] bin/named-sdb
# SDB Berkeley DB - needs to be ported to DB4!
#cp -fp contrib/sdb/bdb/bdb.[ch] bin/named_sdb
# SDB dir
cp -fp contrib/sdb/dir/dirdb.[ch] bin/named-sdb
# SDB tools
mkdir -p bin/sdb_tools
cp -fp %{SOURCE30} bin/sdb_tools/ldap2zone.c
cp -fp %{SOURCE7} bin/sdb_tools/Makefile.in
#cp -fp contrib/sdb/bdb/zone2bdb.c bin/sdb_tools
cp -fp contrib/sdb/ldap/{zone2ldap.1,zone2ldap.c} bin/sdb_tools
cp -fp contrib/sdb/pgsql/zonetodb.c bin/sdb_tools
cp -fp contrib/sdb/sqlite/zone2sqlite.c bin/sdb_tools
%patch12 -p1 -b .sdb
%endif
%if %{SDB}
%patch17 -p1 -b .fix_sdb_ldap
%endif
%if %{SDB}
%patch62 -p1 -b .sdb-sqlite-bld
%endif
%patch133 -p1 -b .rh640538
%patch134 -p1 -b .rh669163
%patch135 -p1 -b .libidn4

# Sparc and s390 arches need to use -fPIE
%ifarch sparcv9 sparc64 s390 s390x
for i in bin/named{,-sdb}/{,unix}/Makefile.in; do
  sed -i 's|fpie|fPIE|g' $i
done
%endif

%patch300 -p1
%patch301 -p1
%patch302 -p1
%patch303 -p1
%patch304 -p1
%patch305 -p1
%patch306 -p1

:;

%build
export CFLAGS="$CFLAGS $RPM_OPT_FLAGS"
export CPPFLAGS="$CPPFLAGS -DDIG_SIGCHASE"
export STD_CDEFINES="$CPPFLAGS"

sed -i -e \
's/RELEASEVER=\(.*\)/RELEASEVER=\1-RedHat-%{version}-%{release}/' \
version

libtoolize -c -f; aclocal -I libtool.m4 --force; autoconf -f

%configure \
  --with-libtool \
  --localstatedir=/var \
  --enable-threads \
  --with-geoip \
  --enable-ipv6 \
  --enable-filter-aaaa \
  --enable-rrl \
  --with-pic \
  --disable-static \
  --disable-openssl-version-check \
  --enable-exportlib \
  --with-export-libdir=%{_libdir} \
  --with-export-includedir=%{_includedir} \
  --includedir=%{_includedir}/bind9 \
%if %{PKCS11}
  --enable-native-pkcs11 \
  --with-pkcs11=%{_libdir}/pkcs11/libsofthsm2.so \
%endif
%if %{SDB}
  --with-dlopen=yes \
  --with-dlz-ldap=yes \
  --with-dlz-postgres=no \
  --with-dlz-mysql=no \
  --with-dlz-filesystem=yes \
  --with-dlz-bdb=yes \
%endif
%if %{GSSTSIG}
  --with-gssapi=yes \
  --disable-isc-spnego \
%endif
  --enable-fixed-rrset \
  --with-tuning=large \
  --with-docbook-xsl=%{_datadir}/sgml/docbook/xsl-stylesheets \
;
make %{?_smp_mflags}

# Regenerate dig.1 manpage
pushd bin/dig
make man
popd
pushd bin/python
make man
popd

%if %{test}
%check
if [ "`whoami`" = 'root' ]; then
  set -e
  chmod -R a+rwX .
  pushd bin/tests
  pushd system
  ./ifconfig.sh up
  popd
  make test
  e=$?
  pushd system
  ./ifconfig.sh down
  popd
  popd
  if [ "$e" -ne 0 ]; then
    echo "ERROR: this build of BIND failed 'make test'. Aborting."
    exit $e;
  fi;
else
  echo 'only root can run the tests (they require an ifconfig).'
%endif

%install
rm -rf ${RPM_BUILD_ROOT}

# Build directory hierarchy
mkdir -p ${RPM_BUILD_ROOT}/etc/logrotate.d
mkdir -p ${RPM_BUILD_ROOT}%{_libdir}/bind
mkdir -p ${RPM_BUILD_ROOT}/var/named/{slaves,data,dynamic}
mkdir -p ${RPM_BUILD_ROOT}%{_mandir}/{man1,man5,man8}
mkdir -p ${RPM_BUILD_ROOT}/run/named
mkdir -p ${RPM_BUILD_ROOT}/var/log

#chroot
mkdir -p ${RPM_BUILD_ROOT}/%{chroot_prefix}/{dev,etc,var,run/named}
mkdir -p ${RPM_BUILD_ROOT}/%{chroot_prefix}/var/{log,named,tmp}

# create symlink as it is on real filesystem
pushd ${RPM_BUILD_ROOT}/%{chroot_prefix}/var
ln -s ../run run
popd

mkdir -p ${RPM_BUILD_ROOT}/%{chroot_prefix}/etc/{pki/dnssec-keys,named}
mkdir -p ${RPM_BUILD_ROOT}/%{chroot_prefix}/%{_libdir}/bind
# these are required to prevent them being erased during upgrade of previous
touch ${RPM_BUILD_ROOT}/%{chroot_prefix}/dev/null
touch ${RPM_BUILD_ROOT}/%{chroot_prefix}/dev/random
touch ${RPM_BUILD_ROOT}/%{chroot_prefix}/dev/zero
touch ${RPM_BUILD_ROOT}/%{chroot_prefix}/etc/named.conf
#end chroot

#sdb-chroot
%if %{SDB}
mkdir -p ${RPM_BUILD_ROOT}/%{chroot_sdb_prefix}/{dev,etc,var,run/named}
mkdir -p ${RPM_BUILD_ROOT}/%{chroot_sdb_prefix}/var/{log,named,tmp}

# create symlink as it is on real filesystem
pushd ${RPM_BUILD_ROOT}/%{chroot_sdb_prefix}/var
ln -s ../run run
popd

mkdir -p ${RPM_BUILD_ROOT}/%{chroot_sdb_prefix}/etc/{pki/dnssec-keys,named}
mkdir -p ${RPM_BUILD_ROOT}/%{chroot_sdb_prefix}/%{_libdir}/bind
# these are required to prevent them being erased during upgrade of previous
touch ${RPM_BUILD_ROOT}/%{chroot_sdb_prefix}/dev/null
touch ${RPM_BUILD_ROOT}/%{chroot_sdb_prefix}/dev/random
touch ${RPM_BUILD_ROOT}/%{chroot_sdb_prefix}/dev/zero
touch ${RPM_BUILD_ROOT}/%{chroot_sdb_prefix}/etc/named.conf
%endif
#end sdb-chroot

make DESTDIR=${RPM_BUILD_ROOT} install

# Remove unwanted files
rm -f ${RPM_BUILD_ROOT}/etc/bind.keys

# Systemd unit files
mkdir -p ${RPM_BUILD_ROOT}%{_unitdir}
install -m 644 %{SOURCE37} ${RPM_BUILD_ROOT}%{_unitdir}
install -m 644 %{SOURCE38} ${RPM_BUILD_ROOT}%{_unitdir}
install -m 644 %{SOURCE44} ${RPM_BUILD_ROOT}%{_unitdir}
install -m 644 %{SOURCE46} ${RPM_BUILD_ROOT}%{_unitdir}

%if %{SDB}
install -m 644 %{SOURCE39} ${RPM_BUILD_ROOT}%{_unitdir}
install -m 644 %{SOURCE40} ${RPM_BUILD_ROOT}%{_unitdir}
install -m 644 %{SOURCE45} ${RPM_BUILD_ROOT}%{_unitdir}
%endif
%if %{PKCS11}
install -m 644 %{SOURCE47} ${RPM_BUILD_ROOT}%{_unitdir}
%endif

mkdir -p ${RPM_BUILD_ROOT}%{_libexecdir}
install -m 755 %{SOURCE41} ${RPM_BUILD_ROOT}%{_libexecdir}/setup-named-chroot.sh
install -m 755 %{SOURCE42} ${RPM_BUILD_ROOT}%{_libexecdir}/generate-rndc-key.sh

install -m 644 %SOURCE3 ${RPM_BUILD_ROOT}/etc/logrotate.d/named
mkdir -p ${RPM_BUILD_ROOT}%{_sysconfdir}/sysconfig
install -m 644 %{SOURCE1} ${RPM_BUILD_ROOT}%{_sysconfdir}/sysconfig/named
%if %{SDB}
mkdir -p ${RPM_BUILD_ROOT}/etc/openldap/schema
install -m 644 %{SOURCE8} ${RPM_BUILD_ROOT}/etc/openldap/schema/dnszone.schema
install -m 644 %{SOURCE12} contrib/sdb/pgsql/
%endif

# Install isc/errno2result.h header
install -m 644 lib/isc/unix/errno2result.h ${RPM_BUILD_ROOT}%{_includedir}/isc

# Files required to run test-suite outside of build tree:
cp -fp config.h ${RPM_BUILD_ROOT}/%{_includedir}/bind9
cp -fp lib/dns/include/dns/forward.h ${RPM_BUILD_ROOT}/%{_includedir}/dns
cp -fp lib/isc/unix/include/isc/keyboard.h ${RPM_BUILD_ROOT}/%{_includedir}/isc

# Remove libtool .la files:
find ${RPM_BUILD_ROOT}/%{_libdir} -name '*.la' -exec '/bin/rm' '-f' '{}' ';';

# Remove -devel files out of buildroot if not needed
%if !%{DEVEL}
rm -f ${RPM_BUILD_ROOT}/%{_libdir}/bind9/*so
rm -rf ${RPM_BUILD_ROOT}/%{_includedir}/bind9
rm -f ${RPM_BUILD_ROOT}/%{_mandir}/man1/isc-config.sh.1*
rm -f ${RPM_BUILD_ROOT}/%{_mandir}/man3/lwres*
rm -f ${RPM_BUILD_ROOT}/%{_bindir}/isc-config.sh
%endif

# SDB manpages
%if %{SDB}
install -m 644 %{SOURCE31} ${RPM_BUILD_ROOT}%{_mandir}/man1/ldap2zone.1
install -m 644 %{SOURCE32} ${RPM_BUILD_ROOT}%{_mandir}/man8/named-sdb.8
install -m 644 %{SOURCE33} ${RPM_BUILD_ROOT}%{_mandir}/man1/zonetodb.1
install -m 644 %{SOURCE34} ${RPM_BUILD_ROOT}%{_mandir}/man1/zone2sqlite.1
%endif

# PKCS11 versions manpages
%if %{PKCS11}
pushd ${RPM_BUILD_ROOT}%{_mandir}/man8
ln -s named.8.gz named-pkcs11.8.gz
ln -s dnssec-checkds.8.gz dnssec-checkds-pkcs11.8.gz
ln -s dnssec-coverage.8.gz dnssec-coverage-pkcs11.8.gz
ln -s dnssec-dsfromkey.8.gz dnssec-dsfromkey-pkcs11.8.gz
ln -s dnssec-keyfromlabel.8.gz dnssec-keyfromlabel-pkcs11.8.gz
ln -s dnssec-keygen.8.gz dnssec-keygen-pkcs11.8.gz
ln -s dnssec-revoke.8.gz dnssec-revoke-pkcs11.8.gz
ln -s dnssec-settime.8.gz dnssec-settime-pkcs11.8.gz
ln -s dnssec-signzone.8.gz dnssec-signzone-pkcs11.8.gz
ln -s dnssec-verify.8.gz dnssec-verify-pkcs11.8.gz
ln -s dnssec-importkey.8.gz dnssec-importkey-pkcs11.8.gz
popd
%endif

# Ghost config files:
touch ${RPM_BUILD_ROOT}%{_localstatedir}/log/named.log

# configuration files:
tar -C ${RPM_BUILD_ROOT} -xjf %{SOURCE28}
touch ${RPM_BUILD_ROOT}/etc/rndc.key
touch ${RPM_BUILD_ROOT}/etc/rndc.conf
mkdir ${RPM_BUILD_ROOT}/etc/named
install -m 644 bind.keys ${RPM_BUILD_ROOT}/etc/named.iscdlv.key
install -m 644 %{SOURCE36} ${RPM_BUILD_ROOT}/etc/trusted-key.key

# sample bind configuration files for %%doc:
mkdir -p sample/etc sample/var/named/{data,slaves}
install -m 644 %{SOURCE25} sample/etc/named.conf
# Copy default configuration to %%doc to make it usable from system-config-bind
install -m 644 ${RPM_BUILD_ROOT}/etc/named.conf named.conf.default
install -m 644 ${RPM_BUILD_ROOT}/etc/named.rfc1912.zones sample/etc/named.rfc1912.zones
install -m 644 ${RPM_BUILD_ROOT}/var/named/{named.ca,named.localhost,named.loopback,named.empty}  sample/var/named
for f in my.internal.zone.db slaves/my.slave.internal.zone.db slaves/my.ddns.internal.zone.db my.external.zone.db; do
  echo '@ in soa localhost. root 1 3H 15M 1W 1D
  ns localhost.' > sample/var/named/$f;
done
:;

mkdir -p ${RPM_BUILD_ROOT}%{_tmpfilesdir}
install -m 644 %{SOURCE35} ${RPM_BUILD_ROOT}%{_tmpfilesdir}/named.conf

mkdir -p ${RPM_BUILD_ROOT}%{_sysconfdir}/rwtab.d
install -m 644 %{SOURCE43} ${RPM_BUILD_ROOT}%{_sysconfdir}/rwtab.d/named

%pre
if [ "$1" -eq 1 ]; then
  /usr/sbin/groupadd -g %{bind_gid} -f -r named >/dev/null 2>&1 || :;
  /usr/sbin/useradd  -u %{bind_uid} -r -N -M -g named -s /sbin/nologin -d /var/named -c Named named >/dev/null 2>&1 || :;
fi;
:;

%post
/sbin/ldconfig
%systemd_post named.service
if [ "$1" -eq 1 ]; then
  # Initial installation
  [ -x /sbin/restorecon ] && /sbin/restorecon /etc/rndc.* /etc/named.* >/dev/null 2>&1 ;
  # rndc.key has to have correct perms and ownership, CVE-2007-6283
  [ -e /etc/rndc.key ] && chown root:named /etc/rndc.key
  [ -e /etc/rndc.key ] && chmod 0640 /etc/rndc.key
fi
:;

%preun
# Package removal, not upgrade
%systemd_preun named.service

%postun
/sbin/ldconfig
# Package upgrade, not uninstall
%systemd_postun_with_restart named.service

%if %{SDB}
%post sdb
# Initial installation
%systemd_post named-sdb.service

%preun sdb
# Package removal, not upgrade
%systemd_preun named-sdb.service

%postun sdb
# Package upgrade, not uninstall
%systemd_postun_with_restart named-sdb.service
%endif

%if %{PKCS11}
%post pkcs11
# Initial installation
%systemd_post named-pkcs11.service

%preun pkcs11
# Package removal, not upgrade
%systemd_preun named-pkcs11.service

%postun pkcs11
# Package upgrade, not uninstall
%systemd_postun_with_restart named-pkcs11.service
%endif

%triggerpostun -n bind -- bind <= 32:9.5.0-20.b1
if [ "$1" -gt 0 ]; then
  [ -e /etc/rndc.key ] && chown root:named /etc/rndc.key
  [ -e /etc/rndc.key ] && chmod 0640 /etc/rndc.key
fi
:;

%triggerun -- bind < 32:9.9.0-0.6.rc1
/sbin/chkconfig --del named >/dev/null 2>&1 || :
/bin/systemctl try-restart named.service >/dev/null 2>&1 || :

%post libs -p /sbin/ldconfig

%postun libs -p /sbin/ldconfig

%post libs-lite -p /sbin/ldconfig

%postun libs-lite -p /sbin/ldconfig

%pre chroot
# updating
if [ "$1" -gt 1 ]; then
    # if %%{chroot_prefix}/var/run is a directory, remove it
    # fix for Bug #1091341
    if [ -d %{chroot_prefix}/var/run ]; then
        rm -rf %{chroot_prefix}/var/run
    fi
fi

%post chroot
%systemd_post named-chroot.service
if [ "$1" -gt 0 ]; then
  [ -e %{chroot_prefix}/dev/random ] || \
    /bin/mknod %{chroot_prefix}/dev/random c 1 8
  [ -e %{chroot_prefix}/dev/zero ] || \
    /bin/mknod %{chroot_prefix}/dev/zero c 1 5
  [ -e %{chroot_prefix}/dev/null ] || \
    /bin/mknod %{chroot_prefix}/dev/null c 1 3
fi;
:;

%posttrans chroot
if [ -x /usr/sbin/selinuxenabled ] && /usr/sbin/selinuxenabled; then
  [ -x /sbin/restorecon ] && /sbin/restorecon %{chroot_prefix}/dev/* > /dev/null 2>&1;
fi;
:;

%preun chroot
%systemd_preun named-chroot.service
if [ "$1" -eq 0 ]; then
  # Package removal, not upgrade
  rm -f %{chroot_prefix}/dev/{random,zero,null}
fi
:;

%postun chroot
# Package upgrade, not uninstall
%systemd_postun_with_restart named-chroot.service


%if %{SDB}

%post sdb-chroot
%systemd_post named-sdb-chroot.service
if [ "$1" -gt 0 ]; then
  [ -e %{chroot_sdb_prefix}/dev/random ] || \
    /bin/mknod %{chroot_sdb_prefix}/dev/random c 1 8
  [ -e %{chroot_sdb_prefix}/dev/zero ] || \
    /bin/mknod %{chroot_sdb_prefix}/dev/zero c 1 5
  [ -e %{chroot_sdb_prefix}/dev/null ] || \
    /bin/mknod %{chroot_sdb_prefix}/dev/null c 1 3
fi;
:;

%posttrans sdb-chroot
if [ -x /usr/sbin/selinuxenabled ] && /usr/sbin/selinuxenabled; then
  [ -x /sbin/restorecon ] && /sbin/restorecon %{chroot_sdb_prefix}/dev/* > /dev/null 2>&1;
fi;
:;

%preun sdb-chroot
%systemd_preun named-sdb-chroot.service
if [ "$1" -eq 0 ]; then
  # Package removal, not upgrade
  rm -f %{chroot_sdb_prefix}/dev/{random,zero,null}
fi
:;

%postun sdb-chroot
# Package upgrade, not uninstall
%systemd_postun_with_restart named-sdb-chroot.service

%endif

%clean
rm -rf ${RPM_BUILD_ROOT}
:;

%files
%defattr(-,root,root,-)
%{_libdir}/bind
%config(noreplace) %verify(not md5 size mtime) %{_sysconfdir}/sysconfig/named
%config(noreplace) %attr(0644,root,named) %{_sysconfdir}/named.iscdlv.key
%config(noreplace) %attr(0644,root,named) %{_sysconfdir}/named.root.key
%{_tmpfilesdir}/named.conf
%{_sysconfdir}/rwtab.d/named
%{_unitdir}/named.service
%{_unitdir}/named-setup-rndc.service
%{_sbindir}/arpaname
%{_sbindir}/ddns-confgen
%{_sbindir}/genrandom
%{_sbindir}/named-journalprint
%{_sbindir}/nsec3hash
%{_sbindir}/dnssec*
%exclude %{_sbindir}/dnssec*pkcs11
%{_sbindir}/named-check*
%{_sbindir}/lwresd
%{_sbindir}/named
%{_sbindir}/rndc*
%{_sbindir}/named-compilezone
%{_sbindir}/isc-hmac-fixup
%{_libexecdir}/generate-rndc-key.sh
%{_mandir}/man1/arpaname.1*
%{_mandir}/man5/named.conf.5*
%{_mandir}/man5/rndc.conf.5*
%{_mandir}/man8/rndc.8*
%{_mandir}/man8/named.8*
%{_mandir}/man8/lwresd.8*
%{_mandir}/man8/dnssec*.8*
%exclude %{_mandir}/man8/dnssec*-pkcs11.8*
%{_mandir}/man8/named-checkconf.8*
%{_mandir}/man8/named-checkzone.8*
%{_mandir}/man8/named-compilezone.8*
%{_mandir}/man8/rndc-confgen.8*
%{_mandir}/man8/ddns-confgen.8*
%{_mandir}/man8/genrandom.8*
%{_mandir}/man8/named-journalprint.8*
%{_mandir}/man8/nsec3hash.8*
%{_mandir}/man8/isc-hmac-fixup.8*
%doc CHANGES README named.conf.default
%doc doc/arm/*html doc/arm/*pdf
%doc sample/

# Hide configuration
%defattr(0640,root,named,0750)
%dir %{_sysconfdir}/named
%dir %{_localstatedir}/named
%config(noreplace) %verify(not link) %{_sysconfdir}/named.conf
%config(noreplace) %verify(not link) %{_sysconfdir}/named.rfc1912.zones
%config %verify(not link) %{_localstatedir}/named/named.ca
%config %verify(not link) %{_localstatedir}/named/named.localhost
%config %verify(not link) %{_localstatedir}/named/named.loopback
%config %verify(not link) %{_localstatedir}/named/named.empty
%defattr(0660,named,named,0770)
%dir %{_localstatedir}/named/slaves
%dir %{_localstatedir}/named/data
%dir %{_localstatedir}/named/dynamic
%ghost %{_localstatedir}/log/named.log
%defattr(0640,root,named,0750)
%ghost %config(noreplace) %{_sysconfdir}/rndc.key
# ^- rndc.key now created on first install only if it does not exist
# %%verify(not size,not md5) %%config(noreplace) %%attr(0640,root,named) /etc/rndc.conf
# ^- Let the named internal default rndc.conf be used -
#    rndc.conf not required unless it differs from default.
%ghost %config(noreplace) %{_sysconfdir}/rndc.conf
# ^- The default rndc.conf which uses rndc.key is in named's default internal config -
#    so rndc.conf is not necessary.
%config(noreplace) %{_sysconfdir}/logrotate.d/named
%defattr(-,named,named,-)
%dir /run/named

%if %{SDB}
%files sdb
%defattr(-,root,root,-)
%{_unitdir}/named-sdb.service
%{_mandir}/man1/zone2ldap.1*
%{_mandir}/man1/ldap2zone.1*
%{_mandir}/man1/zonetodb.1*
%{_mandir}/man1/zone2sqlite.1*
%{_mandir}/man8/named-sdb.8*
%doc contrib/sdb/ldap/README.ldap contrib/sdb/ldap/INSTALL.ldap contrib/sdb/pgsql/README.sdb_pgsql
%dir %{_sysconfdir}/openldap/schema
%config(noreplace) %{_sysconfdir}/openldap/schema/dnszone.schema
%{_sbindir}/named-sdb
%{_sbindir}/zone2ldap
%{_sbindir}/ldap2zone
%{_sbindir}/zonetodb
%{_sbindir}/zone2sqlite
%endif

%files libs
%defattr(-,root,root,-)
%{_libdir}/*so.*
%exclude %{_libdir}/*export.so.*
%exclude %{_libdir}/*pkcs11.so.*
%exclude %{_libdir}/*pkcs11-export.so.*

%files libs-lite
%defattr(-,root,root,-)
%{_libdir}/*export.so.*
%exclude %{_libdir}/*pkcs11-export.so.*

%files license
%defattr(-,root,root,-)
%doc COPYRIGHT

%files utils
%defattr(-,root,root,-)
%{_bindir}/dig
%{_bindir}/host
%{_bindir}/nslookup
%{_bindir}/nsupdate
%{_mandir}/man1/host.1*
%{_mandir}/man1/nsupdate.1*
%{_mandir}/man1/dig.1*
%{_mandir}/man1/nslookup.1*
%{_sysconfdir}/trusted-key.key

%if %{DEVEL}
%files devel
%defattr(-,root,root,-)
%{_libdir}/*so
%exclude %{_libdir}/*export.so
%exclude %{_libdir}/*pkcs11.so
%exclude %{_libdir}/*pkcs11-export.so
%{_includedir}/bind9
%exclude %{_includedir}/bind9/pkcs11
%exclude %{_includedir}/bind9/pk11
%{_mandir}/man1/isc-config.sh.1*
%{_mandir}/man3/lwres*
%{_bindir}/isc-config.sh
%endif

%files lite-devel
%defattr(-,root,root,-)
%{_libdir}/*export.so
%exclude %{_libdir}/*pkcs11-export.so
%{_includedir}/dns
%{_includedir}/dst
%{_includedir}/irs
%{_includedir}/isc
%{_includedir}/isccfg

%files chroot
%defattr(-,root,root,-)
%{_unitdir}/named-chroot.service
%{_unitdir}/named-chroot-setup.service
%{_libexecdir}/setup-named-chroot.sh
%ghost %{chroot_prefix}/dev/null
%ghost %{chroot_prefix}/dev/random
%ghost %{chroot_prefix}/dev/zero
%defattr(0640,root,named,0750)
%dir %{chroot_prefix}
%dir %{chroot_prefix}/dev
%dir %{chroot_prefix}/etc
%dir %{chroot_prefix}/etc/named
%dir %{chroot_prefix}/etc/pki
%dir %{chroot_prefix}/etc/pki/dnssec-keys
%dir %{chroot_prefix}/var
%dir %{chroot_prefix}/run
%dir %{chroot_prefix}/var/named
%ghost %config(noreplace) %{chroot_prefix}/etc/named.conf
%defattr(-,root,root,-)
%dir %{chroot_prefix}/usr
%dir %{chroot_prefix}/%{_libdir}
%dir %{chroot_prefix}/%{_libdir}/bind
%defattr(0660,named,named,0770)
%dir %{chroot_prefix}/var/tmp
%dir %{chroot_prefix}/var/log
%defattr(-,named,named,-)
%dir %{chroot_prefix}/run/named
%{chroot_prefix}/var/run

%if %{SDB}
%files sdb-chroot
%defattr(-,root,root,-)
%{_unitdir}/named-sdb-chroot.service
%{_unitdir}/named-sdb-chroot-setup.service
%{_libexecdir}/setup-named-chroot.sh
%ghost %{chroot_sdb_prefix}/dev/null
%ghost %{chroot_sdb_prefix}/dev/random
%ghost %{chroot_sdb_prefix}/dev/zero
%defattr(0640,root,named,0750)
%dir %{chroot_sdb_prefix}
%dir %{chroot_sdb_prefix}/dev
%dir %{chroot_sdb_prefix}/etc
%dir %{chroot_sdb_prefix}/etc/named
%dir %{chroot_sdb_prefix}/etc/pki
%dir %{chroot_sdb_prefix}/etc/pki/dnssec-keys
%dir %{chroot_sdb_prefix}/var
%dir %{chroot_sdb_prefix}/run
%dir %{chroot_sdb_prefix}/var/named
%ghost %config(noreplace) %{chroot_sdb_prefix}/etc/named.conf
%defattr(-,root,root,-)
%dir %{chroot_sdb_prefix}/usr
%dir %{chroot_sdb_prefix}/%{_libdir}
%dir %{chroot_sdb_prefix}/%{_libdir}/bind
%defattr(0660,named,named,0770)
%dir %{chroot_sdb_prefix}/var/tmp
%dir %{chroot_sdb_prefix}/var/log
%defattr(-,named,named,-)
%dir %{chroot_sdb_prefix}/run/named
%{chroot_sdb_prefix}/var/run
%endif

%if %{PKCS11}
%files pkcs11
%defattr(-,root,root,-)
%{_sbindir}/named-pkcs11
%{_unitdir}/named-pkcs11.service
%{_mandir}/man8/named-pkcs11.8*

%files pkcs11-utils
%defattr(-,root,root,-)
%{_sbindir}/dnssec*pkcs11
%{_sbindir}/pkcs11-destroy
%{_sbindir}/pkcs11-keygen
%{_sbindir}/pkcs11-list
%{_sbindir}/pkcs11-tokens
%{_mandir}/man8/pkcs11*.8*
%{_mandir}/man8/dnssec*-pkcs11.8*

%files pkcs11-libs
%defattr(-,root,root,-)
%{_libdir}/*pkcs11.so.*
%{_libdir}/*pkcs11-export.so.*

%files pkcs11-devel
%defattr(-,root,root,-)
%{_includedir}/bind9/pk11
%{_includedir}/bind9/pkcs11
%{_libdir}/*pkcs11.so
%{_libdir}/*pkcs11-export.so

%endif

%changelog
* Thu Jan 02 2025 Deli Zhang <deli.zhang@citrix.com> - 9.9.4-63
- Add epoch 32

* Tue Sep 24 2024 Deli Zhang <deli.zhang@citrix.com> - 9.9.4-62
- First imported release

