#
# Conditional build:
%bcond_without	tests # do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define	pdir	File
%define	pnam	Random
Summary:	File::Random - Perl module for random selecting of a file
Summary(pl):	File::Random - modu³ Perla do losowego wyboru pliku
Name:		perl-File-Random
Version:	0.17
Release:	4
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	4138133bf7fb0a2b4400073a3f1cea1d
BuildRequires:	perl-devel >= 1:5.8.0
%if %{with tests}
BuildRequires:	perl(Want)
BuildRequires:	perl-Set-Scalar
BuildRequires:	perl-Test-Class
BuildRequires:	perl-Test-Exception
BuildRequires:	perl-Test-ManyParams
BuildRequires:	perl-Test-Simple
BuildRequires:	perl-Test-Warn
%endif
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This module simplifies the routine job of selecting a random file.
(As you can find at CGI scripts).

The simple standard job of selecting a random line from a file is
implemented, too.

%description -l pl
Ten modu³ upraszcza rutynowe zadanie wyboru losowego pliku (które
mo¿na znale¼æ w skryptach CGI). Ma zaimplementowane tak¿e inne proste,
standardowe zadanie - wyboru losowej linii z pliku.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor

%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{perl_vendorlib}/%{pdir}/*.pm
%{_mandir}/man3/*
