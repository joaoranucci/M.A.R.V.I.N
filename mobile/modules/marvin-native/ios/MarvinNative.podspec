Pod::Spec.new do |s|
  s.name = 'MarvinNative'
  s.version = '0.1.0'
  s.summary = 'Pinned gateway transport and interruptible audio for MARVIN Mobile'
  s.description = 'URLSession with SHA-256 SPKI verification, uploads, long polling and AVAudioSession routing.'
  s.author = 'MARVIN'
  s.homepage = 'https://github.com/joaoranucci/M.A.R.V.I.N'
  s.license = { :type => 'MIT', :file => '../../../LICENSE' }
  s.platforms = { :ios => '16.4' }
  s.source = { :git => 'https://github.com/joaoranucci/M.A.R.V.I.N.git' }
  s.swift_version = '5.0'
  s.static_framework = true
  s.dependency 'ExpoModulesCore'
  s.frameworks = 'AVFoundation', 'Security', 'CryptoKit'
  s.source_files = 'MarvinNativeModule.swift', 'MarvinAudioSession.swift', 'MarvinCertificate.swift', 'MarvinTransport.swift'
end
