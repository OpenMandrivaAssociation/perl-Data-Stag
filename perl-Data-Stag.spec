%define module	Data-Stag
%define name	perl-%{module}
%define version 0.11
%define release %mkrel 2

Name:		%{name}
Version:	%{version}
Release:	%{release}
Summary:	%{module} module for perl
License:	GPL or Artistic
Group:		Development/Perl
Source:		http://search.cpan.org/CPAN/authors/id/C/CM/CMUNGALL/%{module}-%{version}.tar.bz2
Url:		http://search.cpan.org/dist/%{module}/
%if %{mdkversion} < 1010
Buildrequires:	perl-devel
%endif
Buildrequires:  perl-IO-String
Buildarch:	noarch
BuildRoot:	%{_tmppath}/%{name}-%{version}

%description
This module is for manipulating data as recursively nested tag/value
pairs (Structured TAGs or Simple Tree AGgreggates). These datastructures
can be represented as nested arrays, which have the advantage of being
native to perl.

%prep
%setup -q -n %{module}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make

%install
rm -rf %{buildroot}
%makeinstall_std

%check
%{__make} test

%clean 
rm -rf %{buildroot}

%files 
%defattr(-,root,root)
%doc INSTALL README Changes
%{_bindir}/*
%{perl_vendorlib}/Data
%{_mandir}/*/*

