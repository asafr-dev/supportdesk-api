# Relationship to `supportdesk-app`

The `supportdesk-app` repo contains a complete end-to-end SupportDesk implementation (UI + backend in one codebase).

This API service repo is a **minimal service-separated** version of the same domain with only a few endpoints:

- list tickets
- get ticket
- patch ticket status

It is intentionally not a full duplicate of `supportdesk-app`; it's a “clean standalone reimplementation” that demonstrates:

- API design + validation
- database modeling + persistence
- testability + CI
