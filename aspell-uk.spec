%global debug_package %{nil}
%global languagecode uk
%global debug_package %{nil}

Summary:	Ukrainian dictionaries for aspell
Name:		aspell-%{languagecode}
Version:	1.8.0
Release:	1%{?dist}

URL:		http://ispell-uk.sourceforge.net/
Source:		http://freefr.dl.sourceforge.net/project/ispell-uk/spell-uk/%{version}/spell-uk-%{version}.tgz
License:	LGPLv3
Group:		Applications/Text

Requires:	aspell >= 0.60
BuildRequires:	aspell >= 0.60

%if %{defined rhel}
BuildRequires:	perl-Encode
%else
BuildRequires:	perl-encoding
%endif

%description
This is Ukrainian dictionary for spellchecking with aspell program

%prep
%setup -q -n spell-uk-%{version}

%build
make ASPELL_ENC=utf-8 ASPELL_ENC_NAME=utf-8 myspell aspell uk.cwl.gz ukrainian

%install
make install PREFIX="$RPM_BUILD_ROOT"
rm -rf %{buildroot}%{_datadir}/doc/%{name}-%{version}

%files
%defattr(-,root,root)
%doc README README.uk TODO Copyright COPYING.GPL COPYING.LGPL
%{_libdir}/aspell-*/uk*
%{_libdir}/aspell-*/koi8-u-nl*

%changelog
* Mon Apr 18 2016 Arkady L. Shane <ashejn@russianfedora.pro> - 1.8.0-1.R
- update to 1.8.0

* Tue Mar 20 2012 21:05:34 Pavlo Rudyj <paulcarroty@riseup.net> 1.6.5-2
- Fixed spec

* Mon Mar 19 2012 20:47:39 Pavlo Rudyj <paulcarroty@riseup.net> 1.6.5-1
- Fixed Makefile

* Mon May 16 2011 22:11:52 Andriy Rysin <arysin@yahoo.com> 1.6.5
- 4K of new words
- some fixes

* Mon Aug 17 2009 23:11:52 Andriy Rysin <arysin@yahoo.com> 1.6.0
- 15K of new words
- many fixes

* Sat Jan 24 2009 13:00:00 Andriy Rysin <arysin@yahoo.com> 1.5.7
- 1K of new words
- some fixes

* Sun Sep 21 2008 13:00:00 Andriy Rysin <arysin@yahoo.com> 1.5.5
- 2K of new words
- some fixes

* Thu Dec 27 2007 13:00:00 Andriy Rysin <arysin@yahoo.com> 1.5.0
- 3K of new words
- some fixes
- some packaging updates

* Sun May 27 2007 13:00:00 Andriy Rysin <arysin@yahoo.com> 1.4.0
- 10K of new words
- some fixes
- myspell now has triple license: GPL, LGPL and MPL

* Sun Apr 08 2007 06:08:09 Andriy Rysin <arysin@yahoo.com> 1.3.3
- Some updates and mozilla package fixes

* Fri Jan 26 2007 9:23:00 Andriy Rysin <arysin@yahoo.com> 1.3.1
- Some packaging and filenaming fixes

* Fri Jan 26 2007 01:23:00 Andriy Rysin <arysin@yahoo.com> 1.3.0
- Release 1.3.0
- Changed versioning to 3 digits
- Added generation of mozilla xpi package
- Added recognition of grave accent (`) often used as apostrophe
- New words and fixes

* Tue Dec 19 2006 21:18:16 Andriy Rysin <arysin@yahoo.com> 1.2
- Release 1.2
- New words
- Rules and words fixes

* Sat Sep 24 2005 10:37:03 Andriy Rysin <arysin@yahoo.com> 1.1a
- Release 1.1a
- Integration of ispell, aspell and myspell into one source package
