%global pypi_name PyMySQL

%{?scl:%scl_package python-%{pypi_name}}
%{!?scl:%global pkg_name %{name}}
%global python3_pkgversion %{nil}

Name:           %{?scl_prefix}python-%{pypi_name}
Version:        0.9.3
Release:        4%{?dist}
Summary:        Pure-Python MySQL client library

License:        MIT
URL:            https://pypi.python.org/pypi/%{pypi_name}/
Source0:        https://files.pythonhosted.org/packages/source/P/PyMySQL/PyMySQL-%{version}.tar.gz

BuildArch:      noarch

%{?scl:Requires: %{scl}-runtime}
%{?scl:BuildRequires: %{scl}-runtime}
BuildRequires:  %{?scl_prefix}python%{python3_pkgversion}-devel
BuildRequires:  %{?scl_prefix}python%{python3_pkgversion}-setuptools
BuildRequires:  %{?scl_prefix}python%{python3_pkgversion}-cryptography
BuildRequires:  %{?scl_prefix}python%{python3_pkgversion}-rpm-macros
Requires:       %{?scl_prefix}python%{python3_pkgversion}-cryptography

%description
This package contains a pure-Python MySQL client library. The goal of PyMySQL is
to be a drop-in replacement for MySQLdb and work on CPython, PyPy, IronPython
and Jython.


%prep
%{?scl:scl enable %{scl} - << \EOF}
set -ex
%setup -n %{pkg_name}-%{version} -qn %{pypi_name}-%{version}
rm -rf %{pypi_name}.egg-info
# Remove tests files so they are not installed globally.
rm -rf tests
%{?scl:EOF}


%build
%{?scl:scl enable %{scl} - << \EOF}
set -ex
%py3_build
%{?scl:EOF}


%install
%{?scl:scl enable %{scl} - << \EOF}
set -ex
%py3_install
%{?scl:EOF}


%check
%{?scl:scl enable %{scl} - << \EOF}
set -ex
# Tests cannot be launch on koji, they require a mysqldb running.
%{?scl:EOF}


%files
%license LICENSE
%doc README.rst
%{python3_sitelib}/%{pypi_name}-%{version}-py%{python3_version}.egg-info/
%{python3_sitelib}/pymysql/


%changelog
* Thu Feb 06 2020 Tomas Orsava <torsava@redhat.com> - 0.9.3-4
- Import from the python38 module and modified for rh-python38 RHSCL
- Resolves: rhbz#1671025

* Fri Dec 13 2019 Tomas Orsava <torsava@redhat.com> - 0.9.3-3
- Exclude unsupported i686 arch

* Thu Nov 21 2019 Lumír Balhar <lbalhar@redhat.com> - 0.9.3-2
- Adjusted for Python 3.8 module in RHEL 8

* Mon Nov 18 2019 Lumír Balhar <lbalhar@redhat.com> - 0.9.3-1
- New upstream version 0.9.3

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 0.9.2-7
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 0.9.2-6
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sun Dec 02 2018 Julien Enselme <jujens@jujens.eu> - 0.9.2-3
- Remove Python 2 subpackage.

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Jul 06 2018 Itamar Reis Peixoto <itamar@ispbrasil.com.br> - 0.9.2-1
- Update to 0.9.2

* Tue Jul 03 2018 Itamar Reis Peixoto <itamar@ispbrasil.com.br> - 0.9.1-1
- Update to 0.9.1

* Mon Jul 02 2018 Miro Hrončok <mhroncok@redhat.com> - 0.9.0-2
- Rebuilt for Python 3.7

* Sat Jun 30 2018 Julien Enselme <jujens@jujens.eu> - 0.9.0-1
- Update to 0.9.0

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 0.8.1-2
- Rebuilt for Python 3.7

* Mon May 07 2018 Julien Enselme <jujens@jujens.eu> - 0.8.1-1
- Update to 0.8.1

* Mon Mar 19 2018 Carl George <carl@george.computer> - 0.8.0-5
- Rename python3 subpackage to python34

* Thu Feb 15 2018 Itamar Reis Peixoto <itamar@ispbrasil.com.br> - 0.8.0-4
- make spec file compatible with epel7
- remove conditionals and always build for Python 3

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Mon Jan 15 2018 Iryna Shcherbina <ishcherb@redhat.com> - 0.8.0-2
- Update Python 2 dependency declarations to new packaging standards
  (See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3)

* Wed Dec 27 2017 Julien Enselme <jujens@jujens.eu> - 0.8.0-1
- Update to 0.8.0

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.11-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Apr 07 2017 Julien Enselme <jujens@jujens.eu> - 0.7.11-1
- Update to 0.7.11

* Wed Feb 15 2017 Julien Enselme <jujens@jujens.eu> - 0.7.10-1
- Update to 0.7.10

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.9-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Dec 19 2016 Miro Hrončok <mhroncok@redhat.com> - 0.7.9-3
- Rebuild for Python 3.6

* Wed Nov 23 2016 Damien Ciabrini <dciabrin@redhat.com> - 0.7.9-2
- cherrypick commit 755dfdc upstream to allow bind before connect
  Related: rhbz#1378008

* Sun Sep 18 2016 Julien Enselme <jujens@jujens.eu> - 0.7.9-1
- Update to 0.7.9

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6.7-6
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.7-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Mon Jan 4 2016 Julien Enselme <jujens@jujens.eu> - 0.6.7-4
- Correct installation problems due to Requires: mariadb

* Thu Nov 5 2015 Julien Enselme <jujens@jujens.eu> - 0.6.7-3
- Rebuilt for python 3.5

* Wed Nov  4 2015 Haïkel Guémar <hguemar@fedoraproject.org> - 0.6.7-2
- Drop unnecessary mariadb requirement
- Add python3 conditionals in order to rebuild it in EL7

* Thu Oct 1 2015 Julien Enselme <jujens@jujens.eu> - 0.6.7-1
- Update to 0.6.7

* Thu Aug 6 2015 Julien Enselme <jujens@jujens.eu> - 0.6.6-4
- Use %%license in %%files

* Wed Aug 5 2015 Julien Enselme <jujens@jujens.eu> - 0.6.6-3
- Move python2 package in its own subpackage
- Add provides

* Fri Jul 31 2015 Julien Enselme <jujens@jujens.eu> - 0.6.6-2
- Add Provides: python2-PyMySQL
- Remove usage of %%py3dir

* Sun May 31 2015 Julien Enselme <jujens@jujens.eu> - 0.6.6-1
- Update to 0.6.6

* Wed Nov 26 2014 Julien Enselme <jujens@jujens.eu> - 0.6.2-1
- Initial packaging
