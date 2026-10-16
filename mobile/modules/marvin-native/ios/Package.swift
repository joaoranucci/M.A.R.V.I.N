// swift-tools-version: 5.9
import PackageDescription

// Tests the exact certificate and URLSession sources used by the iOS pod.
// This macOS suite does not claim to test an iPhone UI, microphone or audio session.
let package = Package(
  name: "MarvinGatewaySecurity",
  platforms: [.macOS(.v13), .iOS("16.4")],
  products: [.library(name: "MarvinGatewaySecurity", targets: ["MarvinGatewaySecurity"])],
  targets: [
    .target(name: "MarvinGatewaySecurity", path: ".",
      exclude: ["MarvinNativeModule.swift", "MarvinAudioSession.swift", "MarvinNative.podspec", "Tests"],
      sources: ["MarvinCertificate.swift", "MarvinTransport.swift"]),
    .testTarget(name: "MarvinGatewaySecurityTests", dependencies: ["MarvinGatewaySecurity"], path: "Tests")
  ],
  swiftLanguageVersions: [.v5]
)
