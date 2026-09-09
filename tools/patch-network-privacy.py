from pathlib import Path

p = Path('privacy.html')
s = p.read_text()

old = "<p>Relay and network providers necessarily process temporary connection information such as IP addresses while routing traffic. Yamora's signaling relay does not create a persistent database of profiles, exact locations, matches, or message contents. Connection metadata can also be visible to internet and infrastructure providers as necessary to deliver the service.</p>"
new = "<p>Relay and network providers necessarily process temporary connection information such as IP addresses while routing traffic. Yamora's signaling relay does not create a persistent database of profiles, exact locations, matches, or message contents. For direct WebRTC setup, Yamora may contact a public STUN service, which necessarily receives ordinary network information such as the requesting IP address but is not sent the user's Yamora profile, messages, photos, voice introduction, exact location, compatibility data, or peer-session encryption keys. Connection metadata can also be visible to internet and infrastructure providers as necessary to deliver the service.</p>"
assert old in s
s = s.replace(old, new, 1)

old = "<p>On supported mobile browsers, push notifications are off by default and are enabled only after the user chooses to enable them and the browser grants notification permission. Yamora creates a random opaque push-inbox capability and a separate random management secret. The relay associates the browser's PushSubscription with the opaque inbox and stores only a SHA-256 hash of the management secret; it does not register a Yamora profile ID or candidate ID with the push service.</p>"
new = "<p>On supported mobile browsers, push notifications are off by default and are enabled only after the user chooses to enable them and the browser grants notification permission. Yamora creates a random opaque push-inbox capability and a separate random management secret. The relay sends the registration through an authenticated internal service to a MongoDB-backed push registry, which associates the browser's PushSubscription with the opaque inbox and stores only a SHA-256 hash of the management secret; it does not register a Yamora profile ID or candidate ID with the push service.</p>"
assert old in s
s = s.replace(old, new, 1)

old = "<li><a href=\"https://www.mongodb.com/legal/privacy-policy\" rel=\"noopener noreferrer\">MongoDB Atlas</a>, when optional model improvement is enabled in production, for durable storage of explicitly consented model-improvement exports;</li>"
new = "<li><a href=\"https://www.mongodb.com/legal/privacy-policy\" rel=\"noopener noreferrer\">MongoDB Atlas</a> for durable storage of opaque mobile push registrations and, when optional model improvement is enabled in production, explicitly consented model-improvement exports. The push registry contains an opaque inbox identifier, a SHA-256 management-token hash, browser PushSubscription data, and timestamps rather than Yamora profile identities or message contents;</li>"
assert old in s
s = s.replace(old, new, 1)

needle = "<li><a href=\"https://www.bigdatacloud.com/privacy\" rel=\"noopener noreferrer\">BigDataCloud</a> for the optional client-side city/area lookup. Yamora sends a rounded approximately 2 km location point rather than the exact device coordinates; the provider also receives normal network information such as IP address as part of delivering the request;</li>"
assert needle in s
cloudflare = "<li><a href=\"https://www.cloudflare.com/privacypolicy/\" rel=\"noopener noreferrer\">Cloudflare</a> for the public STUN service used to improve direct WebRTC NAT traversal. Cloudflare necessarily receives ordinary connection metadata such as IP address for the STUN request; Yamora does not intentionally send dating-profile content, messages, photos, voice introductions, exact location, compatibility data, browsing-derived data, or peer-session encryption keys to the STUN service;</li>"
s = s.replace(needle, needle + "\n        " + cloudflare, 1)

old = "<p>Yamora uses HTTPS and WSS for server transmission, authenticated encrypted peer sessions, strict server-side schemas, installation-bound collector credentials when model contribution is enabled, durable database controls for contributed data, signed and expiring model envelopes, staged rollout, monitoring, and automatic rollback where the corresponding production services are configured. No system can guarantee absolute security.</p>"
new = "<p>Yamora uses HTTPS and WSS for server transmission, authenticated encrypted peer sessions, strict server-side schemas, capability-bounded push registration, installation-bound collector credentials when model contribution is enabled, durable database controls for opaque push registrations and contributed data, signed and expiring model envelopes, staged rollout, monitoring, and automatic rollback where the corresponding production services are configured. No system can guarantee absolute security.</p>"
assert old in s
s = s.replace(old, new, 1)

p.write_text(s)
