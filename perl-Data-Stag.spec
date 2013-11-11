%define upstream_name	 Data-Stag
%define upstream_version 0.14

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	1

Summary:	%{upstream_name} module for perl
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}/
Source0:	http://search.cpan.org/CPAN/authors/id/C/CM/CMUNGALL/Data-Stag-%{upstream_version}.tar.gz

BuildRequires:	perl-devel
BuildRequires:	perl-IO-String
BuildArch:	noarch

%description
This module is for manipulating data as recursively nested tag/value
pairs (Structured TAGs or Simple Tree AGgreggates). These datastructures
can be represented as nested arrays, which have the advantage of being
native to perl.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make

%install
%makeinstall_std

%check
make test

%files 
%doc INSTALL README Changes
%{_bindir}/*
%{perl_vendorlib}/Data
%{_mandir}/*/*


%changelog
* Sun May 29 2011 Funda Wang <fwang@mandriva.org> 0.110.0-2mdv2011.0
+ Revision: 681381
- mass rebuild

* Wed Jul 29 2009 JÃ©rÃ´me Quelin <jquelin@mandriva.org> 0.110.0-1mdv2011.0
+ Revision: 403085
- rebuild using %%perl_convert_version

* Fri Aug 08 2008 Thierry Vignaud <tv@mandriva.org> 0.11-2mdv2009.0
+ Revision: 268410
- rebuild early 2009.0 package (before pixel changes)

* Fri Jun 06 2008 Guillaume Rousse <guillomovitch@mandriva.org> 0.11-1mdv2009.0
+ Revision: 216415
- update to new version 0.11

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Sat Sep 15 2007 Guillaume Rousse <guillomovitch@mandriva.org> 0.10-3mdv2008.0
+ Revision: 86328
- rebuild


* Thu Aug 31 2006 Guillaume Rousse <guillomovitch@mandriva.org> 0.10-2mdv2007.0
- Rebuild

* Mon Dec 19 2005 Guillaume Rousse <guillomovitch@mandriva.org> 0.10-1mdk
- New release 0.10
- dropped patch 0 (fixed upstream)

* Thu Oct 20 2005 Rafael Garcia-Suarez <rgarciasuarez@mandriva.com> 0.09-4mdk
- Fix typo in package name (patch 0)

* Mon Oct 10 2005 Nicolas Lécureuil <neoclust@mandriva.org> 0.09-3mdk
- Fix BuildRequires
- %%mkrel

* Tue Jun 07 2005 Guillaume Rousse <guillomovitch@mandriva.org> 0.09-2mdk 
- spec cleanup
- don't ship useless empty directories
- make est in %%check

* Thu May 26 2005 Rafael Garcia-Suarez <rgarciasuarez@mandriva.com> 0.09-1mdk
- 0.09

* Sat Feb 12 2005 Rafael Garcia-Suarez <rgarciasuarez@mandrakesoft.com> 0.08-1mdk
- 0.08

* Mon Dec 20 2004 Guillaume Rousse <guillomovitch@mandrake.org> 0.06-2mdk
- fix buildrequires in a backward compatible way

* Wed Jul 21 2004 Guillaume Rousse <guillomovitch@mandrake.org> 0.06-1mdk 
- new version

* Wed Apr 21 2004 Guillaume Rousse <guillomovitch@mandrake.org> 0.05-1mdk
- new version
- rpmbuildupdate aware
- macros
- make test

* Wed Feb 25 2004 Guillaume Rousse <guillomovitch@mandrake.org> 0.03-2mdk
- fixed dir ownership (distlint)



