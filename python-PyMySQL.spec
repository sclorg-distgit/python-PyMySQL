%global pypi_name PyMySQL
%{?scl:%scl_package python-%{pypi_name}}
%{!?scl:%global pkg_name %{name}}

Name:           %{?scl_prefix}python-%{pypi_name}
Version:        0.7.5
Release:        1%{?dist}
Summary:        Pure-Python MySQL client library

License:        MIT
URL:            https://pypi.python.org/pypi/%{pypi_name}/
Source0:        https://files.pythonhosted.org/packages/source/P/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{pkg_name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildArch:      noarch
BuildRequires:  %{?scl_prefix}python-devel
BuildRequires:  %{?scl_prefix}python-setuptools

%description
This package contains a pure-Python MySQL client library. The goal of PyMySQL
is to be a drop-in replacement for MySQLdb and work on CPython, PyPy,
IronPython and Jython.


%prep
%setup -qn %{pypi_name}-%{version}
rm -rf %{pypi_name}.egg-info


%build
%{?scl:scl enable %{scl} - << \EOF}
%{__python3} setup.py build
%{?scl:EOF}


%install
%{?scl:scl enable %{scl} - << \EOF}
%{__python3} setup.py install --skip-build --root %{buildroot}
# Remove shebang
for lib in %{buildroot}%{python3_sitelib}/pymysql/tests/thirdparty/test_MySQLdb/*.py; do
  sed -i '1{\@^#!/usr/bin/env python@d}' $lib
done
%{?scl:EOF}


%files
%doc README.rst LICENSE
%{python3_sitelib}/%{pypi_name}-%{version}-py%{python3_version}.egg-info/
%{python3_sitelib}/pymysql/


%changelog
* Wed Jul 27 2016 Tomas Orsava <torsava@redhat.com> - 0.7.5-1
- Specfile taken from Fedora, modified for use with SCLs
- Updated to latest upstream version

