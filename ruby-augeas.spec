Summary:	Ruby bindings for augeas
Summary(pl.UTF-8):	Wiązania języka Ruby do augeasa
Name:		ruby-augeas
Version:	0.4.1
Release:	1
License:	LGPL v2.1+
Source0:	http://augeas.net/download/ruby/%{name}-%{version}.tgz
# Source0-md5:	b7d059cdcbe8b78727b08882b7128ba7
Group:		Development/Languages
URL:		http://augeas.net/
BuildRequires:	rpmbuild(macros) >= 1.484
BuildRequires:	ruby >= 1:1.8.1
BuildRequires:	ruby-rake
%{?ruby_mod_ver_requires_eq}
#BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

# nothing to be placed there. we're not noarch only because of ruby packaging
%define		_enable_debug_packages	0

%description
Ruby bindings for augeas.

%description -l pl.UTF-8
Wiązania języka Ruby do augeasa.

%prep
%setup -q

sed -i -e 's,"make","%{__make} CC=\\"%{__cc}\\" CFLAGS=\\"%{rpmcflags} -fPIC\\"",' Rakefile

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
