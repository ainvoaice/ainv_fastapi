INSERT INTO plans (id, plan_code, plan_name, plan_price, plan_features)
VALUES
(
    '11111111-1111-4111-8111-111111111111',
    'plan1',
    'Team of One',
    'free',
    '[
        "Up to 2 invoices per month",
        "Full library of professional templates",
        "AI-driven invoices, items & clients",
        "PDF export, email delivery, and sharing",
        "Branded invoices with your logo and style",
        "One-click invoice duplication",
        "Email support"
    ]'::jsonb
),
(
    '10111111-1111-4111-8111-111111111111',
    'plan10',
    'Team of Ten',
    'US$10 / month',
    '[
        "Up to 100 invoices per month",
        "Full library of professional templates",
        "AI-driven invoices, items & clients",
        "PDF export, email delivery, and sharing",
        "Branded invoices with your logo and style",
        "One-click invoice duplication",
        "Priority support"
    ]'::jsonb
),
(
    '10011111-1111-4111-8111-111111111111',
    'plan100',
    'Team of Hundred',
    'US$100 / month',
    '[
        "AI Agents",
        "Advanced Billing",
        "Custom solutions available"
    ]'::jsonb
);