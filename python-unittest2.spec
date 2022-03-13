%define	module	unittest2

Name:           python-%{module}
Version:        1.1.0
Release:        3
Summary:        Backport of new unittest features for Python 2.7 to Python 2.4+
Group:          Development/Python
License:        BSD
URL:            http://pypi.python.org/pypi/unittest2
Source0:        http://pypi.python.org/packages/source/u/%{module}/%{module}-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  python-devel
BuildRequires:  python-setuptools
BuildRequires:  python3dist(wheel)
BuildRequires:  python3dist(pip)
%rename		python3-unittest2

%description
unittest2 is a backport of the new features added to the unittest
testing framework in Python 2.7. It has been tested to on Python 2.4 -
2.6.

To use unittest2 instead of unittest simply replace ``import
unittest`` with ``import unittest2``.

Classes in unittest2 derive from the equivalent classes in unittest,
so it should be possible to use the unittest2 test running infra-
structure without having to switch all your tests to using unittest2
immediately. Similarly, you can use the new assert methods on
``unittest2.TestCase`` with the standard unittest test running
infrastructure. Not all of the new features in unittest2 will work
with the standard unittest test loaders and runners, however.


%prep
%setup -q -n %{module}-%{version}

%install
%py_install

%files -f FILE_LIST
%doc README.txt
%{python_sitelib}/unittest2/*




%changelog
* Wed Sep 14 2011 Lev Givon <lev@mandriva.org> 0.5.1-3mdv2011.0
+ Revision: 699811
- Clean up spec file.
- imported package python-unittest2

