%global cartridgedir %{_libexecdir}/openshift/cartridges/patton

Name:          openshift-origin-cartridge-patton
Version:       1.0
Release:       1%{?dist}
Summary:       WiserTogether Patton cartridge
Group:         Development/Languages
License:       ASL 2.0
URL:           https://www.openshift.com
Source0:       http://mirror.openshift.com/pub/openshift-origin/source/%{name}/%{name}-%{version}.tar.gz
Requires:      facter
Requires:      rubygem(openshift-origin-node)
Requires:      openshift-origin-node-util
Requires:      scl-utils
BuildRequires: scl-utils-build
Requires:      python27
Requires:      mod_wsgi >= 3.2
Requires:      mod_wsgi < 3.4
Requires:      httpd < 2.4

Requires:      MySQL-python
Requires:      pymongo
Requires:      pymongo-gridfs
Requires:      python-magic

Requires:      python27-MySQL-python
Requires:      python27-python-psycopg2
Requires:      python27-mod_wsgi
Requires:      python27-python-pip-virtualenv
Requires:      python27-numpy

Requires:      libjpeg
Requires:      libjpeg-devel
Requires:      libcurl
Requires:      libcurl-devel
Requires:      numpy
Requires:      numpy-f2py
Requires:      gcc-gfortran
Requires:      freetype-devel
Requires:      atlas-devel
Requires:      lapack-devel
Requires:      redhat-lsb-core
Requires:      ta-lib-devel
Requires:      symlinks

BuildArch:     noarch

%description
WiserTogether Patton cartridge for OpenShift. (Cartridge
format V2)


%prep
%setup -q

%build
%__rm %{name}.spec

%install
%__mkdir -p %{buildroot}%{cartridgedir}
%__cp -r * %{buildroot}%{cartridgedir}

%__mkdir -p %{buildroot}%{cartridgedir}/env

%__mv %{buildroot}%{cartridgedir}/metadata/manifest.yml

%__mkdir -p %{buildroot}%{cartridgedir}/usr/versions/2.7
%__cp -anv %{buildroot}%{cartridgedir}/usr/versions/shared/* %{buildroot}%{cartridgedir}/usr/versions/2.7/

%__rm -rf %{buildroot}%{cartridgedir}/usr/versions/shared

%files
%dir %{cartridgedir}
%attr(0755,-,-) %{cartridgedir}/bin/
%attr(0755,-,-) %{cartridgedir}/usr/versions/2.7/bin/*
%attr(0755,-,-) %{cartridgedir}/usr/versions/3.3/bin/*
%{cartridgedir}
%doc %{cartridgedir}/README.md
%doc %{cartridgedir}/COPYRIGHT
%doc %{cartridgedir}/LICENSE

%changelog
* Tue Nov 25 2013 Baron Chandler <baron.chandler@wisertogether.com> 1.0.0-1
- Yoinked this over from RedHat's python spec.