#
# Conditional build:
# _without_tests - do not perform "make test"
%include	/usr/lib/rpm/macros.perl
%define	pdir	File
%define	pnam	Random
Summary:	File::Random - Perl module for random selecting of a file
#Summary(pl):	
Name:		perl-File-Random
Version:	0.17
Release:	1
License:	GPL/Artistic
Group:		Development/Languages/Perl
Source0:	ftp://ftp.cpan.org/pub/CPAN/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
BuildRequires:	perl >= 5.6
BuildRequires:	rpm-perlprov >= 3.0.3-26
%if %{?_without_tests:0}%{!?_without_tests:1}
BuildRequires:	perl(Want)
BuildRequires:	perl-Test-Simple
BuildRequires:	perl-Test-Exception
BuildRequires:	perl-Test-Class
BuildRequires:	perl-Set-Scalar
BuildRequires:	perl-Test-Warn
BuildRequires:	perl-Test-ManyParams
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This module simplifies the routine job of selecting a random file.
(As you can find at CGI scripts).

The simple standard job of selecting a random line from a file is
implemented, too.

# %description -l pl
# TODO

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
perl Makefile.PL
%{__make}

%{!?_without_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{perl_sitelib}/%{pdir}/*.pm
%{_mandir}/man3/*
