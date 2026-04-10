# User Bootstrap / Seed Contract (Draft)

Goal: seed demo data immediately after registration so the user sees 3 complete invoices on first login.
This contract is idempotent and safe to call multiple times.

---

## 1) Bootstrap New User

`POST /v1/onboard/bootstrap`

Seeds user profile, business, and demo data (clients, items, taxes, fees, payment methods, invoices + items/payments).

### Headers
- `Authorization: Bearer <supabase_jwt>` (client call)
- `Idempotency-Key: <uuid>` (optional but recommended)

### Request Body
```json
{
  "auth_uid": "uuid-from-supabase-auth",
  "email": "user@example.com",
  "ten_id": "uuid-tenant",
  "owner_id": "uuid-owner", 
  "profile": {
    "u_locale": "en-US",
    "u_type": "free202509"
  }
}
```

### Response (200)
```json
{
  "ok": true,
  "seeded": true,
  "zme_id": "uuid",
  "biz_id": "uuid",
  "demo_invoice_ids": ["uuid", "uuid", "uuid"]
}
```

### Notes
- `ten_id` and `owner_id` are required for RLS.  
- In the current DB model, `owner_id == zme.id`.  
- The endpoint should:
  1. Ensure `zme` exists (create if missing).
  2. Ensure business exists (create if missing).
  3. If invoices already exist for the biz, return `seeded=false`.
  4. Otherwise seed demo dataset.

---

## 2) Optional Cleanup for Unconfirmed Users

`POST /v1/onboard/cleanup`

Deletes demo data for a user who never confirmed email.

### Headers
- `Authorization: Bearer <service_key>` (server-only)

### Request Body
```json
{
  "auth_uid": "uuid-from-supabase-auth"
}
```

### Response (200)
```json
{
  "ok": true,
  "deleted": true
}
```

---

## 3) Health Check

`GET /v1/onboard/health`

### Response (200)
```json
{ "ok": true }
```
