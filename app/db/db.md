React
   ↓
supabase.auth.signUp
   ↓
auth.users
   ↓
Postgres trigger
   ↓
zme row created
   ↓
RLS controls access



create policy "user read own row"
on public.zme
for select
to authenticated
using (supabase_uid = auth.uid());



Flow summary
Login → Supabase Auth (or your trigger + zme)
Populates initial state into Zustand
Zustand → frontend session state
Controls current values for the UI
Updates immediately when user changes display info, preferences, etc.
Acts as the source of truth for the session
Postgres (zme or related tables) → persistent storage
Persists user info until next login
Can be updated via explicit frontend action (Edge Function, FastAPI, etc.)
Optional: read from DB to refresh Zustand if needed
Benefits
Fast UI updates → no network latency for session changes
Clear persistence layer → Postgres is authoritative between sessions
No unnecessary JWT refreshes or backend calls for display info
Safe RLS / auth control through Supabase when needed

This is essentially Firebase-style caching + Supabase RLS + Postgres persistence, but cleaner for multi-table Option B architecture.