#
# Conditional build:
%bcond_with	tests	# unit tests (some fail on python2)
%bcond_without	python2 # CPython 2.x module
%bcond_without	python3 # CPython 3.x module

Summary:	Coloured output for nosetests
Summary(pl.UTF-8):	Kolorowe wyjście z testów nose
Name:		python-rednose
Version:	1.3.0
Release:	3
License:	MIT
Group:		Libraries/Python
#Source0Download: https://pypi.org/simple/rednose/
Source0:	https://files.pythonhosted.org/packages/source/r/rednose/rednose-%{version}.tar.gz
# Source0-md5:	11f9d74f6a7241093afa6529f2c2f282
Patch0:		%{name}-colorama.patch
URL:		https://pypi.org/project/rednose/
%if %{with python2}
BuildRequires:	python-modules >= 1:2.7
BuildRequires:	python-setuptools
%if %{with tests}
BuildRequires:	python-nose
BuildRequires:	python-six >= 1.10.0
BuildRequires:	python-termstyle >= 0.1.7
%endif
%endif
%if %{with python3}
BuildRequires:	python3-modules >= 1:3.4
BuildRequires:	python3-setuptools
%if %{with tests}
BuildRequires:	python3-nose
BuildRequires:	python3-six >= 1.10.0
BuildRequires:	python3-termstyle >= 0.1.7
%endif
%endif
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.714
Requires:	python-modules >= 1:2.7
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
rednose is a nosetests plugin for adding colour (and readability) to
nosetest console results.

%description -l pl.UTF-8
rednose to wtyczka testów nose dodająca kolorowanie (i czytelność) do
wyników testów na konsoli.

%package -n python3-rednose
Summary:	Coloured output for nosetests
Summary(pl.UTF-8):	Kolorowe wyjście z testów nose
Group:		Libraries/Python
Requires:	python3-modules >= 1:3.4

%description -n python3-rednose
rednose is a nosetests plugin for adding colour (and readability) to
nosetest console results.

%description -n python3-rednose -l pl.UTF-8
rednose to wtyczka testów nose dodająca kolorowanie (i czytelność) do
wyników testów na konsoli.

%prep
%setup -q -n rednose-%{version}
%patch0 -p1

%build
%if %{with python2}
%py_build %{?with_tests:test}
%endif

%if %{with python3}
%py3_build %{?with_tests:test}
%endif

%install
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%py_install

%{__rm} -r $RPM_BUILD_ROOT%{py_sitescriptdir}/test_files
%py_postclean
%endif

%if %{with python3}
%py3_install

%{__rm} -r $RPM_BUILD_ROOT%{py3_sitescriptdir}/test_files
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%files
%defattr(644,root,root,755)
%doc LICENCE readme.rst
%{py_sitescriptdir}/rednose.py[co]
%{py_sitescriptdir}/rednose-%{version}-py*.egg-info
%endif

%if %{with python3}
%files -n python3-rednose
%defattr(644,root,root,755)
%doc LICENCE readme.rst
%{py3_sitescriptdir}/rednose.py
%{py3_sitescriptdir}/__pycache__/rednose.cpython-*.py[co]
%{py3_sitescriptdir}/rednose-%{version}-py*.egg-info
%endif
