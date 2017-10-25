Summary:	Ruby bindings for augeas
Summary(pl.UTF-8):	Wiązania języka Ruby do augeasa
Name:		ruby-augeas
Version:	0.5.0
Release:	4
License:	LGPL v2.1+
Source0:	http://download.augeas.net/ruby/%{name}-%{version}.tgz
# Source0-md5:	a132eace43ce13ccd059e22c0b1188ac
Group:		Development/Languages
URL:		http://augeas.net/
BuildRequires:	augeas-devel
BuildRequires:	pkgconfig
BuildRequires:	rpmbuild(macros) >= 1.484
BuildRequires:	ruby >= 1:1.8.1
BuildRequires:	ruby-rake
BuildRequires:	sed >= 4.0
%{?ruby_mod_ver_requires_eq}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Ruby bindings for augeas.

%description -l pl.UTF-8
Wiązania języka Ruby do augeasa.

%prep
%setup -q

%{__sed} -i -e 's@"make"@"%{__make} CC=\\"%{__cc}\\" CFLAGS=\\"%{rpmcflags} -fPIC $(pkg-config --cflags augeas)\\""@' Rakefile

%build
rake build

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{ruby_rubylibdir},%{ruby_archdir}}

cp -p lib/augeas.rb $RPM_BUILD_ROOT%{ruby_archdir}
cp -p ext/augeas/_augeas.so $RPM_BUILD_ROOT%{ruby_rubylibdir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc NEWS README.rdoc
%attr(755,root,root) %{ruby_rubylibdir}/_augeas.so
%{ruby_archdir}/augeas.rb
