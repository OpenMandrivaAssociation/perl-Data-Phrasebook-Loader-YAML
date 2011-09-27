# $Id: perl-Data-Phrasebook-Loader-YAML.spec 7981 2009-11-03 03:05:34Z dag $
# Authority: dries
# Upstream: Barbie <barbie$cpan,org>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Data-Phrasebook-Loader-YAML

Summary: Absract your phrases with YAML
Name: perl-Data-Phrasebook-Loader-YAML
Version: 0.09
Release: %mkrel 1
License: Artistic/GPL
Group: Development/Perl
URL: http://search.cpan.org/dist/Data-Phrasebook-Loader-YAML/
Source: http://www.cpan.org/modules/by-module/Data/Data-Phrasebook-Loader-YAML-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
BuildArch: noarch
BuildRequires: perl
BuildRequires: perl(ExtUtils::MakeMaker)
BuildRequires: perl(Test::More) >= 0.47

%description
Absract your phrases with YAML.

%prep
%setup -q -n %{real_name}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS="vendor" PREFIX="%{buildroot}%{_prefix}"
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__make} pure_install

### Clean up buildroot
find %{buildroot} -name .packlist -exec %{__rm} {} \;

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc Artistic COPYING Changes INSTALL LICENSE MANIFEST MANIFEST.SKIP META.yml README
%doc %{_mandir}/man3/Data::Phrasebook::Loader::YAML.3pm*
%dir %{perl_vendorlib}/Data/
%dir %{perl_vendorlib}/Data/Phrasebook/
%dir %{perl_vendorlib}/Data/Phrasebook/Loader/
#%{perl_vendorlib}/Data/Phrasebook/Loader/YAML/
%{perl_vendorlib}/Data/Phrasebook/Loader/YAML.pm

%changelog
* Thu Nov 08 2007 Dag Wieers <dag@wieers.com> - 0.09-1 - 7981/dag
- Updated to release 0.09.

* Sun Nov 19 2006 Dries Verachtert <dries@ulyssis.org> - 0.06-1
- Initial package.
