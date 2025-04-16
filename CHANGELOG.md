# CHANGELOG



## v0.3.1 (2025-04-17)

### Ci

* ci: update github action ([`264be4f`](https://github.com/cemlyn007/apple-gpu/commit/264be4f895df40efe93b16958c94e467c55b86ad))

* ci: only publish to github if the version changes ([`21e56c6`](https://github.com/cemlyn007/apple-gpu/commit/21e56c63b678076185c7d03a176619d0476821b2))

* ci: try local git config ([`69363d4`](https://github.com/cemlyn007/apple-gpu/commit/69363d426e5765c48868d7203f055f48b64a5dec))

* ci: try changing git config location ([`4a7069d`](https://github.com/cemlyn007/apple-gpu/commit/4a7069d86536519f0ce5f9377e3a3e200b5119d8))

* ci: wrap python version in quotes ([`6843ce7`](https://github.com/cemlyn007/apple-gpu/commit/6843ce7c55ebd4b5edd8004293d022dc0a97469b))

* ci: remove 3.13.0-alpha.1 because pyobc doesn&#39;t have wheels for it ([`54c9d96`](https://github.com/cemlyn007/apple-gpu/commit/54c9d966b0d507aa2da2b8ffbfab57c691184154))

* ci: correct python-version 3.13.0 to 3.13.0-alpha.1 ([`b75a2f9`](https://github.com/cemlyn007/apple-gpu/commit/b75a2f94219813d4807a8eb4b14dbd0aedf631c1))

* ci: only test python 3.10 to 3.13 due to self-hosted limitation ([`141f5fc`](https://github.com/cemlyn007/apple-gpu/commit/141f5fc174f3cf306ea5e8d068388bfd9675b964))

* ci: actions run on self-hosted ([`4165442`](https://github.com/cemlyn007/apple-gpu/commit/41654425d35d3f9e37d559915d13923984ebaf69))

* ci: only upload to pypi if a dist folder exists ([`60297a2`](https://github.com/cemlyn007/apple-gpu/commit/60297a2df611246efc6469f94712bce723fbdb43))

* ci: fix `TWINE_REPOSITORY` ([`3f7efcb`](https://github.com/cemlyn007/apple-gpu/commit/3f7efcbfdfc1cf25c505e62dfa9fee1a91c7d3d4))

### Fix

* fix: memory leak when calling the function multiple times ([`b29be02`](https://github.com/cemlyn007/apple-gpu/commit/b29be027d370b9e9f96798f9a3444bba71c82e01))


## v0.3.0 (2023-10-20)

### Ci

* ci: publish to pypi ([`af0d0e6`](https://github.com/cemlyn007/apple-gpu/commit/af0d0e6ee7168dfa7625bcf4e26aea29442d0dd5))

### Feature

* feat: add urls ([`10595c7`](https://github.com/cemlyn007/apple-gpu/commit/10595c70006497822c67e82071c5b53012cb7d8f))


## v0.2.0 (2023-10-20)

### Ci

* ci: update release workflow ([`975a90a`](https://github.com/cemlyn007/apple-gpu/commit/975a90af4f959ecc3f96f06a0f14bae88e32b7d5))

### Feature

* feat: add license ([`e072b2d`](https://github.com/cemlyn007/apple-gpu/commit/e072b2d2f481cd3182a387354a369ac27a3eb034))


## v0.1.0 (2023-10-20)

### Ci

* ci: publish ([`7fd1b67`](https://github.com/cemlyn007/apple-gpu/commit/7fd1b6737e3e17243f05997d5b596333cbd3f392))

* ci: workflow ([`fb4a470`](https://github.com/cemlyn007/apple-gpu/commit/fb4a470937903de23de40fbedbad920764e951b7))

* ci: change action used for release ([`74d59f4`](https://github.com/cemlyn007/apple-gpu/commit/74d59f4339fe580d48d8647e0d20ca542161b730))

* ci: rename workflow into workflows ([`d74aa67`](https://github.com/cemlyn007/apple-gpu/commit/d74aa678d5d52d1ff48d83a872d5df211aac8f96))

* ci: try semantic release ([`5614132`](https://github.com/cemlyn007/apple-gpu/commit/5614132b3c6b1b9e076132ed99cf2ea335f9eb95))

### Feature

* feat: make package ([`a4978c2`](https://github.com/cemlyn007/apple-gpu/commit/a4978c2c10f227037753e2317e849a21195ca121))

* feat: allow python 3.8 and greater ([`ebcf269`](https://github.com/cemlyn007/apple-gpu/commit/ebcf2695d7e9de870b6bcc15e16ece320a32f379))

* feat: `accelerator_performance_statistics` ([`ea9ef56`](https://github.com/cemlyn007/apple-gpu/commit/ea9ef56686a1a5fb3f0abf41077a9f39735a744d))

### Fix

* fix: add future annotations for python 3.8 ([`25aebef`](https://github.com/cemlyn007/apple-gpu/commit/25aebefe1f4e4da7b29bd77497c673deef483984))

* fix: pyobj dependency should be pyobjc ([`bb38c6b`](https://github.com/cemlyn007/apple-gpu/commit/bb38c6b95bfd16256f1d3397dda8a45e66280d8d))

### Refactor

* refactor: restructure `accelerator_performance_statistics` ([`517b009`](https://github.com/cemlyn007/apple-gpu/commit/517b009573e8888fc9388aabc240c9aefa761634))

* refactor: move `test_apple_gpu.py` into `tests` folder ([`c1d5b4a`](https://github.com/cemlyn007/apple-gpu/commit/c1d5b4ac77b69830a00932bf2a26dd37e3b2aa90))
