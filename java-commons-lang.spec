Summary:	Jakarta Commons Lang
Name:		jakarta-commons-lang
Version:	1.0.1
Release:	0.1
License:	Apache
Group:		Development/Languages/Java
Source0:	http://jakarta.apache.org/builds/jakarta-commons/release/commons-lang/v1.0.1/commons-lang-%{version}-src.tar.gz
# Source0-md5:	7217632e6a7f18770734128baba273c2
URL:		http://jakarta.apache.org/
BuildRequires:	jakarta-ant >= 1.5
Requires:	jre
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_javalibdir	/usr/share/java

%description
Jakarta Commons Lang.

%description -l pl
Jakarta Commons Lang.

%prep
%setup -q -n commons-lang-%{version}-src

%build
cd lang
cp LICENSE.txt ../LICENSE
ant dist

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_javalibdir}

install lang/dist/*.jar $RPM_BUILD_ROOT%{_javalibdir}
ln -sf commons-lang-%{version}.jar $RPM_BUILD_ROOT%{_javalibdir}/commons-lang.jar

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc lang/dist/LICENSE lang/dist/RELEASE-NOTES.txt lang/dist/docs/api
%{_javalibdir}/*.jar
