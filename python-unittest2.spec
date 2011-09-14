%define	module	unittest2
%define	name	python-%{module}
%define version	0.5.1
%define release	%mkrel 3

Name:           %{name}
Version:        %{version}
Release:        %{release}
Summary:        Backport of new unittest features for Python 2.7 to Python 2.4+
Group:          Development/Python
License:        BSD
URL:            http://pypi.python.org/pypi/unittest2
Source0:        http://pypi.python.org/packages/source/u/%{module}/%{module}-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildArch:      noarch
BuildRequires:  python-devel
BuildRequires:  python-setuptools

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
rm -rf %{buildroot}
PYTHONDONTWRITEBYTECODE= %{__python} setup.py install --root %{buildroot} --record=FILE_LIST

%clean
rm -rf %{buildroot}

%files -f FILE_LIST
%defattr(-,root,root,-)
%doc README.txt


