%bcond_without check
%global goipath  github.com/dsnet/compress
%global commit   cc9eb1d7ad760af14e8f918698f745e80377af4f
Version: 0

%global common_description %{expand:
This repository hosts a collection of compression related libraries. The goal of
this project is to provide pure Go implementations for popular compression
algorithms beyond what the Go standard library provides. The goals for these
packages are as follows:
* Maintainable: That the code remains well documented, well tested, readable,    
  easy to maintain, and easy to verify that it conforms to the specification    
  for the format being implemented.
* Performant: To be able to compress and decompress within at least 80% of the
  rates that the C implementations are able to achieve.
* Flexible: That the code provides low-level and fine granularity control over
  the compression streams similar to what the C APIs would provide.

Of these three, the first objective is often at odds with the other two
objectives and provides interesting challenges. Higher performance can often be
achieved by muddling abstraction layers or using non-intuitive low-level
primitives. Also, more features and functionality, while useful in some
situations, often complicates the API. Thus, this package will attempt to
satisfy all the goals, but will defer to favoring maintainability when the
performance or flexibility benefits are not significant enough.}

%gometa

Name: %{goname}
Release: 0.3%{?dist}
Summary: Collection of compression related Go packages
License: BSD
URL: %{gourl}
Source0: %{gosource}
# https://github.com/dsnet/compress/pull/63
Patch0: 0001-fix-bench-test-on-32bit-architectures.patch
%if %{with check}
BuildRequires: brotli-devel
BuildRequires: bzip2-devel
BuildRequires: golang(github.com/dsnet/golib/unitconv)
BuildRequires: golang(github.com/klauspost/compress/flate)
BuildRequires: golang(github.com/ulikunitz/xz/lzma)
BuildRequires: libzstd-devel
BuildRequires: xz-devel
BuildRequires: zlib-devel
%endif

%description
%{common_description}

%package devel
Summary: %{summary}
BuildArch: noarch

%description devel
%{common_description}

This package contains the source code needed for building packages that import
the %{goipath} Go namespace.

%package doc
Summary: %{summary} - documentation
BuildArch: noarch

%description doc
%{common_description}

This package contains the documentations.

%prep
%gosetup -q
%patch0 -p1

%install
%goinstall

%if %{with check}
%check
%gochecks
%endif

%files devel -f devel.file-list
%license LICENSE.md
%doc README.md

%files doc
%doc doc/*

%changelog
* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.3.gitcc9eb1d
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Mar 28 2018 Dominik Mierzejewski <dominik@greysector.net> - 0-0.2.20180326gitcc9eb1d
- split docs into a separate subpackage

* Mon Mar 26 2018 Dominik Mierzejewski <dominik@greysector.net> - 0-0.1.20180326gitcc9eb1d
- First package for Fedora
