Pod::Spec.new do |s|
  s.name           = 'MarvinNative'
  s.version        = '0.1.0'
  s.summary        = 'MARVIN native helpers (stubs on iOS in v0.1)'
  s.description    = 'Certificate pinning, audio session and share intake for MARVIN Mobile.'
  s.author         = 'MARVIN'
  s.homepage       = 'https://example.invalid/marvin'
  s.platforms      = { :ios => '16.4' }
  s.source         = { git: '' }
  s.static_framework = true
  s.dependency 'ExpoModulesCore'
  s.source_files = '**/*.{h,m,swift}'
end
