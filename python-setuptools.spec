%define module	setuptools
 
Summary:	Python Distutils Enhancements
Name:		python-%{module}
Version:	0.6.30
Release:	1.auto
License:	Zope Public License (ZPL)
Group:		Development/Python
Url:		http://pypi.python.org/pypi/distribute
Source0:        http://pypi.python.org/packages/source/d/distribute/distribute-%{version}.tar.gz
BuildArch:	noarch
BuildRequires:	python-devel
Requires:	python-devel
Requires:	python-pkg-resources
BuildRoot:	%{_tmppath}/%{name}-%{version}-buildroot

%description
A collection of enhancements to the Python distutils that allow 
you to more easily build and distribute Python packages, especially 
ones that have dependencies on other packages.

%package -n python-pkg-resources
Summary: Runtime module to access python resources
Group:	Development/Python
Conflicts: python-setuptools < 0.6c9-2mdv

%description -n python-pkg-resources
Module used to find and manage Python package/version dependencies and access
bundled files and resources, including those inside of zipped .egg files.

%prep
%setup -q -n distribute-%{version}

%build
export CFLAGS="%{optflags}"
%__python setup.py build

%check
%__python setup.py test

%install
%__rm -rf %{buildroot}
%__python setup.py install --root=%{buildroot}

%clean
%__rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc *.txt
%{_bindir}/*
%{py_sitedir}/*
%exclude %{py_sitedir}/pkg_resources.py*

%files -n python-pkg-resources
%defattr(-,root,root)
%{py_sitedir}/pkg_resources.py*


%changelog
* Sun May 01 2011 Lev Givon <lev@mandriva.org> 0.6.16-1mdv2011.0
+ Revision: 661111
- Update to 0.6.16.

* Mon Nov 01 2010 Funda Wang <fwang@mandriva.org> 0.6.14-4mdv2011.0
+ Revision: 591551
- wrong req on python-sqlalchemy

* Sun Oct 31 2010 Funda Wang <fwang@mandriva.org> 0.6.14-3mdv2011.0
+ Revision: 591061
- add requires on python-sqlalchemy for tuntime

* Sat Oct 30 2010 Andrey Borzenkov <arvidjaar@mandriva.org> 0.6.14-2mdv2011.0
+ Revision: 590349
- rebuild with new python 2.7

* Fri Oct 29 2010 Funda Wang <fwang@mandriva.org> 0.6.14-1mdv2011.0
+ Revision: 589963
- New fork distribute

* Sat Nov 07 2009 Frederik Himpe <fhimpe@mandriva.org> 0.6c11-1mdv2010.1
+ Revision: 462167
- Update to non-broken version 0.6c11

* Mon Oct 19 2009 Lev Givon <lev@mandriva.org> 0.6c10-1mdv2010.1
+ Revision: 458285
- Update to 0.6c10.

* Wed Dec 24 2008 Michael Scherer <misc@mandriva.org> 0.6c9-3mdv2009.1
+ Revision: 318435
- rebuild for new python

* Fri Nov 28 2008 Wanderlei Cavassin <cavassin@mandriva.com.br> 0.6c9-2mdv2009.1
+ Revision: 307480
- Splitted python-pkg-resources, then packages like elisa will not
  need to drag python-devel and others.

* Mon Oct 27 2008 Lev Givon <lev@mandriva.org> 0.6c9-1mdv2009.1
+ Revision: 297704
- Update to 0.6c9.
  Remove patch (included in 0.6c9).

  + Tomasz Pawel Gajc <tpg@mandriva.org>
    - remuve stupid redefines
    - fix mixture of tabs and spaces
    - better description
    - export CFLAGS
    - enable checks

* Tue Jul 08 2008 Colin Guthrie <cguthrie@mandriva.org> 0.6c8-3mdv2009.0
+ Revision: 232866
- Apply patch to fix bug when working with subversion 1.5 checkouts

* Sat Jul 05 2008 Funda Wang <fwang@mandriva.org> 0.6c8-2mdv2009.0
+ Revision: 231966
- setuptools requires python2.5/config/Makefile to work

* Thu Feb 21 2008 Lev Givon <lev@mandriva.org> 0.6c8-1mdv2008.1
+ Revision: 173464
- Update to 0.6c8.

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Wed Nov 07 2007 Lev Givon <lev@mandriva.org> 0.6c7-2mdv2008.1
+ Revision: 106628
- Fix file installation issue.

* Thu Oct 11 2007 Lev Givon <lev@mandriva.org> 0.6c7-1mdv2008.1
+ Revision: 97177
- Update to 0.6c7.

* Mon Jun 18 2007 Lev Givon <lev@mandriva.org> 0.6c6-1mdv2008.0
+ Revision: 41112
- Update to 0.6c6.

* Tue Apr 24 2007 Lev Givon <lev@mandriva.org> 0.6c5-1mdv2008.0
+ Revision: 17935
- Update to 0.6c5.


* Fri Jan 05 2007 Michael Scherer <misc@mandriva.org> 0.6c3-1mdv2007.0
+ Revision: 104332
- upgrade to 0.6c3
- use %%rel for mkrel

* Wed Nov 29 2006 Michael Scherer <misc@mandriva.org> 0.6a11-2mdv2007.1
+ Revision: 88724
- rebuild for new python
- Import python-setuptools


