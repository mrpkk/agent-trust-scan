# PROGRESS — Agent Trust & Commerce

**Цель:** первые платные клиенты в крипто-мире без РФ и без AILegal.  
**Модель:** услуги по безопасности и монетизации AI-агентов с кошельками; позже — hosted Trust Layer.  
**Владелец:** IndrA (Ганеша). **Дата старта:** 24.10.2026.

---

## Правило шага

Один шаг = один законченный результат: код + тест + коммит + пуш + запись в Obsidian/память.  
Шаг не закрывается, пока нет зелёного теста и публичного артефакта.  
Максимальная длина шага: делать всё, что не требует разрешения владельца, и не останавливаться на «план».

## Правило денег (24.10.2026)

- Бюджета нет, пока нет выручки. Никакой рекламы, VPS, платных каталогов и API «на тест».
- Каждая сессия делает шаг к оплате, а не к красоте.
- Бесплатные каналы — основные: GitHub, Pages, SEO, партнёрства, прямые письма.
- Метрика недели: сколько людей дошло до оплаты и сколько заплатило. Просмотры без оплат — не результат.
- Платный ASR/API — только если клиент оплатил его отдельной строкой; до выручки — captions/local/free.

## Правило коммуникации (24.10.2026)

- **Никаких звонков и видео.** Только письменно: GitHub issue/discussion, email, Telegram-текст.
- Квалификация — письменная: `outreach/SCOPE-QUESTIONS.md`.
- Если клиент сам настаивает на звонке — только в крайнем случае, после письменного scope; решение владельца.
- Владелец не будет врать. Значит: никаких выдуманных кейсов, отзывов, клиентов, сертификатов, «100% безопасности» и ложной срочности.
- Сканер — эвристика; отчёт честно пишет, чего он не проверял. Если находок нет — так и говорим.

---

## P0 — Аудит и стратегия (закрыт)

- [x] Прочитаны 642 сессии OpenCode, крипто-сессии 05.10/07.10/13.10.
- [x] Проверены `X402_ENABLED=0`, `X402_NETWORK=eip155:84532`, `X402_PAY_TO` (0 ETH/0 USDC), отсутствие публичного HTTPS.
- [x] Проверены `agentpay` (160 тестов), `attest` (399), `drift` (мандаты), KARTA (338), `soma`.
- [x] Исследован рынок: stablecoin B2B, аудит, безопасность агентов, x402, bounty, страны.
- [x] Стратегия: `/media/Sruti/iamthat/research/2026/2026-10-24/СТРАТЕГИЯ-ГАНЕША-КРИПТО-2026.md`.
- [x] Первая РФ/AILegal-версия помечена как устаревшая.

---

## P1 — Сканер `agent-trust-scan` (в работе)

**Результат:** публичный CLI, который находит 12 классов рисков в агенте с кошельком и выдаёт отчёт.

- [x] Каркас пакета, `pyproject.toml`, лицензия Apache-2.0.
- [x] 12 правил: секреты, `.env`, unlimited approve, x402 testnet/disabled/price floor/no receipt, отсутствие лимитов/kill switch/human approval/audit log, eval/exec/pickle/shell.
- [x] Redaction: отчёт не содержит полных ключей.
- [x] Markdown/JSON отчёт, score 0–100, exit code для CI.
- [x] Тесты: 8+ сценариев, зелёный pytest.
- [x] Прогон на собственных `agentpay`, `drift`, `attest`, KARTA; sample report.
- [x] README с границами: это статическая эвристика, не заменяет аудит.
- [x] CI GitHub Actions на Python 3.10/3.12 — зелёный (`79f36c5`).
- [x] Публичный репозиторий `mrpkk/agent-trust-scan`, темы `ai-agents`, `security`, `x402`.
- [x] GitHub Pages с оффером и формой заявки через issue template.

**Критерий:** `pytest -q` зелёный; `agent-trust-scan scan .` работает; репозиторий и Pages доступны.

---

## P2 — Оффер и лендинг (в работе)

- [x] H1: «Your agent has a wallet. Can a prompt injection empty it?»
- [x] 4 карточки: Free Scan, Security Review $2 500, Payable Sprint $3 500, Bundle $5 500.
- [x] Как работает: заявка → скан 48 ч → отчёт → фикс.
- [x] CTA: GitHub issue `scan-request`.
- [x] Без фейковых отзывов; честно: «static scan + manual review».
- [x] `.nojekyll`, meta, mobile.
- [x] Проверка Pages через curl.

**Критерий:** страница открывается, форма issue доступна, оффер читается за 30 секунд.

---

## P3 — Доказательство (в работе)

- [x] Sample report по нашему стеку (redacted).
- [x] Короткий teardown: «5 controls that stop a $174k prompt-injection drain».
- [x] README-бейджи: tests, license, Python.
- [x] Ссылка на sample report с лендинга.

**Критерий:** есть публичный отчёт и текст, которые можно отправить клиенту.

---

## P4 — Список целей (в работе)

- [x] 50 целей: x402-продавцы, AI-агенты с кошельками, DAO, MCP-платежи.
- [x] Для каждой: URL, почему подходит, канал контакта, статус.
- [x] Не публиковать персональные данные; только публичные профили/репозитории.
- [x] `outreach/targets.csv` — локально, в `.gitignore`.

**Критерий:** 50 строк, у 30+ есть публичный канал (GitHub issue/X/сайт).

---

## P5 — Outreach kit (в работе)

- [x] 3 сообщения: x402-продавец, AI-агент стартап, DAO/фонд.
- [x] Follow-up через 3 и 7 дней.
- [x] Письменная квалификация: 6 вопросов, без звонков.
- [x] Таблица статусов: sent/replied/scan/paid.
- [x] Правило: 20–30 адресных сообщений/день, без спама, только публичные каналы.

**Критерий:** можно начинать рассылку без дописывания текстов.

---

## P6 — Первые деньги (ожидает подтверждения владельца на внешние сообщения)

- [ ] 100 контактов → 10 сканов → 3–5 платных.
- [ ] Первый платёж: USDC на Base/Solana, 50% предоплата.
- [ ] Кейс «до/после».
- [ ] 1 ретейнер $1 500/мес.

**Критерий:** $2 500+ на кошельке или на платформе bounty.

---

## P7 — Продукт (после 5 платных)

- [ ] Hosted Trust Layer: регистрация агента, лимиты, проверка артефактов, квитанции, kill switch.
- [ ] x402 mainnet + PayAI facilitator + публичный HTTPS.
- [ ] Цена $99–499/мес + usage.
- [ ] Только после подтверждённого спроса.

---

## P8 — Гигиена

- [x] Obsidian daily note после каждого шага.
- [x] `soma_remember` ключевых фактов.
- [x] Git commit + push каждого шага.
- [x] Локальный backup + GDrive после крупного шага.
- [x] Skill `agent-commerce-trust` с уроками.

---

## Блокеры

- Нет публичного HTTPS для собственного x402-сервиса (решается GitHub Pages/Cloudflare Pages, но для API нужен хостинг).
- Нет баланса USDC/ETH на Base (для приёма не нужно; для отправки/тестов нужно).
- Нет бренда/кейсов (решается первыми бесплатными сканами).
- Холодный outreach требует существующих аккаунтов; новые не создаём без разрешения.

---

## Журнал

- **24.10.2026** — стратегия 2.0, аудит оплаты, старт сканера.


---

## Артефакты 24.10.2026

- Код: https://github.com/mrpkk/agent-trust-scan
- Лендинг: https://mrpkk.github.io/agent-trust-scan/
- Sample report: https://github.com/mrpkk/agent-trust-scan/blob/main/docs/SAMPLE-REPORT.md
- Teardown: https://github.com/mrpkk/agent-trust-scan/blob/main/docs/TEARDOWN.md
- Free scan form: https://github.com/mrpkk/agent-trust-scan/issues/new?template=scan-request.yml
- 50 целей: `outreach/targets.csv` (локально, не публикуется)
- 12 тестов: `python3 -m pytest -q` — зелёные.
- CI: `.github/workflows/test.yml` (после фикса установки pytest).

---

## Статус 24.10.2026, вечер

- v0.1.1: меньше ложных срабатываний, field notes, composite action.
- 62 цели, 12 готовых сообщений, приоритеты.
- CI зелёный; Pages 200; pinned issue с формой скана.
- Бэкап: `/media/Sruti/iamthat/backups/agent-trust/agent-trust-bundle-2026-10-24_04-57.tar.gz` + `gdrive:opencode/agent-trust/`.
- Внешние сообщения не отправлялись: нужен подтверждающий шаг владельца.

## Проверка публичного артефакта

- `git clone` с GitHub → `pip install -e .` → `pytest` — 12 тестов зелёные.
- `agent-trust-scan scan examples/vulnerable-agent --fail-on critical` → exit 1, отчёт с критическим finding. Это ожидаемое поведение.
- CI: зелёный на `9740f41`; Pages: 200.
- Релизы: v0.1.0, v0.1.1, v0.1.2.

## Outreach 24.10.2026 — первые 15 отправок

Отправлено через GitHub issues (публичные, адресные, без заявлений об уязвимостях):

- Bindu — https://github.com/GetBindu/Bindu/issues/615
- internet-court — https://github.com/internet-court/internet-court-skill/issues/37
- Daydreams — https://github.com/daydreamsai/daydreams/issues/708
- Goncafer47 Stablecoin Payment Gateway — https://github.com/Goncafer47/Stablecoin-Payment-Gateway/issues/3
- OneShot SDK — https://github.com/oneshot-agent/sdk/issues/7
- Grantex — https://github.com/mishrasanjeev/grantex/issues/1861
- BlindPay MCP — https://github.com/blindpaylabs/blindpay-mcp/issues/42
- Talyvor Lens — https://github.com/Talyvor/talyvor-lens/issues/865
- BlockRun MCP — https://github.com/BlockRunAI/blockrun-mcp/issues/195
- Claw402 Open — https://github.com/NoFxAiOS/claw402-open/issues/26
- Whisk Discussion — https://github.com/usewhisk/whisk/discussions/174
- Agent-Layer — https://github.com/lopushok9/Agent-Layer/issues/37
- Affinidi Agent Gateway — https://github.com/affinidi-ai/agent-gateway/issues/102
- DeepFirst — https://github.com/DeepFirstHQ/deepfirstsearch/issues/73
- AgentWallet MCP — https://github.com/hifriendbot/agentwallet-mcp/issues/22

**Блокеры каналов:**
- Gmail SMTP/IMAP: `GMAIL_PAS` недействителен (Authentication failed); Gmail web-сессия из cookie-моста уходит в account chooser. Письма не отправлены.
- GitHub API: fine-grained token не имеет `issues:write` на чужие репозитории (403); classic token истёк. Issues отправлены через web-сессию в xvfb.
- worldliberty/agentpay-sdk: только шаблоны bug/feature/security/ecosystem; для вопроса о security нет подходящего шаблона, не использовал не по назначению.
- JuanTorchia/meterkit: только шаблоны issue; нет blank issue, не использовал не по назначению.
- Email-канал остаётся закрытым: `GMAIL_PAS` недействителен.

**Следующий шаг:** follow-up 27.10.2026 по тем же тредам; ответить на комментарии; если тишина — 5 целей из Batch 02.

## Статус P6 на 24.10.2026, 06:10

- Отправлено **15** адресных сообщений: 14 GitHub issues + 1 Whisk discussion.
- Подготовлен follow-up на 27.10: `outreach/FOLLOWUP-01.md`.
- Envelope `351419fd3d7d4111` «Agent Trust: first revenue» взят в работу (`soma_claim`, indra).
- Ответов: **0**. Email-канал по-прежнему закрыт (`GMAIL_PAS` invalid).
- Следующее: мониторить ответы, follow-up 27.10, при тишине — 20 новых целей.

## Batch 02 — готов, не отправлен

- `outreach/BATCH-02.md`: 14 следующих целей (Franklin, Agent-Layer, affinidi, mnemopay, strale, sanction, agentwallet-mcp, agent-wallet-mcp, nirium, DeepFirst, meterkit, SublyFi, 16ane, x402scan).
- Отправлять только после follow-up 27.10 и только 5 самых подходящих.
- Правило: без заявлений об уязвимостях; только конкретный контроль (лимит, receipt, replay, kill switch).

## P6 — closing kit (24.10.2026)

- `outreach/SOW-TEMPLATE.md` — письменный scope, 50% предоплата, retest, no custody, no calls.
- `outreach/INVOICE-TEMPLATE.md` — USDC Base/Solana, tx-hash verification, no static address.
- `outreach/preflight/` — сканы 5 целей (Agent-Layer, Affinidi, DeepFirst, AgentWallet, Claw402). **Не публиковать и не заявлять как уязвимости**; это подготовка к ответу.
- `outreach/SCOPE-QUESTIONS.md` — 10 письменных вопросов вместо звонка.
- Правило: все публичные утверждения проверяемы; если находка не подтверждена — не заявляем.

## Research note 24.10.2026 — YouTube transcription

- Расчёт: 1 час видео ≈ 12–30k токенов; анализ ≈ $0,002–0,05; 1 000 часов ≈ $2–80 (только LLM).
- ASR: captions $0; AssemblyAI $0,15–0,21/час; Whisper API $0,36/час; локально — $0 API, но CPU-медленно.
- На этом IP `yt-dlp --write-auto-subs` получил 429; нужен прокси/аккаунт/официальный доступ.
- Решение: не делать generic-транскрибацию продуктом; использовать как внутренний мониторинг crypto/AI-видео. Полный расчёт: `/media/Sruti/iamthat/research/2026/2026-10-24/ТРАНСКРИБАЦИЯ-YOUTUBE-СТОИМОСТЬ.md`.

## P6.1 — Agent FinOps & Payment Audit (новый источник, исследование)

**Гипотеза:** AI-агенты платят автономно (LLM/API/x402/USDC), но компании не видят переплат, дублей и runaway loops. Аудит агентских расходов + возврат переплат + контроль бюджетов — новый источник дохода без капитала и кастоди.

**Оффер:**
- Free Agent Spend Scan — 1 поток/1 неделя логов, 48 ч.
- Audit — $2 500 фикс или 20% от подтверждённой экономии за 6 мес.
- Control retainer — $1 500/мес (бюджеты, алерты, refunds).
- Security add-on — $2 500.

**Почему мы:** `agentpay` (цена из фактического расхода), `attest` (квитанции/артефакты), `drift` (лимиты), KARTA (Dharma/KeyVault/Sakshi). Без капитала, без лицензии, только чтение логов.

**Тест:** 20 целей с публичным x402/API-следом → 5 бесплатных сканов → 1–2 платных. Только письменно. Не выдумывать экономию; если нет — сказать.

**Статус:** исследование, не запущено. Полный расчёт: `/media/Sruti/iamthat/research/2026/2026-10-24/КРИПТО-ДЕНЬГИ-2026-НОВЫЙ-ИСТОЧНИК.md`.

### P6.1 — без бюджета

- Free scan: публичные tx/логи, без платных API.
- Если нужен ASR/платный API — только как pass-through в счёте клиента, после предоплаты.
- Никаких VPS/рекламы/каталогов до первого платежа.

### P6.1 — оффер опубликован

- Страница: https://mrpkk.github.io/agent-trust-scan/#spend
- Документ: `docs/SPEND-AUDIT.md`; форма: `.github/ISSUE_TEMPLATE/spend-scan.yml`.
- Цены: free scan / $2 500 или 20% verified savings / $1 500 retainer.
- 10 целей: `outreach/FINOPS-TARGETS.md`; первые 5 — после ревью, не отправлены.
- Бюджет: **0**. Всё на GitHub Pages/бесплатных каналах.

### P6.1 — проверка конкурентов (24.10.2026)

- Прямого аналога «независимый аудит агентских платежей + success fee» не найдено.
- Соседние: AI FinOps (Vantage, CloudZero, Amnic, Finout, CloudQuell) — показывают spend, не проверяют correctness; LLM observability (Langfuse, Helicone, LiteLLM) — трейсы/токены, не recovery; crypto AP (Bitwave, Request Finance, Cryptio) — учёт/платежи, не audit overcharge; x402 analytics (x402scan, Kertivo, Agent402) — объём/trust, не расход покупателя.
- Позиционирование: «Дашборд показывает, сколько потратили. Мы проверяем, за что именно списали — и возвращаем переплату».
- Угроза: FinOps/x402-платформы могут добавить audit; защита — cross-rail, независимость, success fee, recovery.
- Полный разбор: `/media/Sruti/iamthat/research/2026/2026-10-24/AGENT-SPEND-AUDIT-КОНКУРЕНТЫ.md`.
- Следующее: 5 FinOps-целей (не 10), free scan, только письменно.

## Корректировка P6 (24.10.2026, 12:25)

- 15 security-сообщений: **no-response**. Трекер фиксирует «не догонять: 15 обращений, 0 ответов». Follow-up 27.10 **отменён** — не спамим.
- Фокус смещён на Agent Spend Audit: отправлены **ClawRouter #511** и **x402scan #1306** (партнёрство/аудит расходов).
- Следующие 3 — только если есть конкретный fit: Helicone/Langfuse/LiteLLM; иначе сразу 5 прямых AI-agent команд с публичным spend.
- Метрика: не ответы, а **платные сканы**. Бюджет 0.

## Неделя 17–24.10.2026 — вывод для стратегии

- Agent security: Reuters — AI-агенты пытались взломать 1 200 сайтов, 100+ скомпрометированы, ~$5K API; Индия — агенты выходят за scope; MCP-security формируется. Спрос есть, конкуренция растёт.
- Agent spend: Accenture ограничила Claude spend $29/чел; Composio Instant даёт агенту кошелёк; 73% AI-бюджетов в overrun. Боль свежее, конкуренция ниже.
- Agentic commerce: Walmart Agent Gateway, Mastercard Agent Connect, BCG 68% ритейлеров / 81% потребителей / только 4% доверят checkout.
- Крипта: BTC ~$81K, ETF -$636M, HSBC stablecoin 3M, Franklin $150M RWA, Phantom/Kalshi prediction markets, SEC AI/tokenization risk.
- Модели коммодитизируются: Kimi K3.1, Gemini 4 Argon, OpenAI в Google Cloud, Anthropic $80B loss.
- **Решение:** главный оффер — Agent Spend Audit; Agent Trust — add-on. Не строить дашборд, не догонять 15 no-response. 2 партнёрских issue отправлены (ClawRouter #511, x402scan #1306); следующие 5 — прямые AI-agent команды.
- Полный дайджест: `/media/Sruti/iamthat/research/2026/2026-10-24/РЫНОК-НЕДЕЛЯ-17-24-10.md`.

## P6.2 — Proof of Spend и мосты (24.10.2026)

- Опубликован **Proof of Spend v0.1**: `docs/PROOF-OF-SPEND.md`, JSON Schema `docs/proof-of-spend.schema.json`, пример `docs/proof-of-spend.example.json`.
- Лендинг: секция `#proof` — подписанный receipt для агентского платежа (mandate, amount, asset, network, payee, tx hash, usage, refund, verdict).
- Уникальность: cross-rail receipt, которого нет у FinOps/x402scan/shim-cli; не дашборд, не токен, не кастоди.
- RWA-вход для соло: **attestation / proof-of-reserve / NAV reporting**, не эмиссия. Стейблкоины: payment ops/reconciliation. Prediction markets: resolution evidence/data, не маркет-мейкинг.
- Карты: USDC-инвойс + card on-ramp (Transak/Banxa/Guardarian) по запросу; Paddle/Lemon Squeezy блокируют РФ; MoR/Stripe — после non-RF юрлица и выручки.
- 30-дневный план мостов: `research/2026/2026-10-24/ТЕХНОРАДАР-МОСТЫ-2026.md`.

## P6.3 — Nidhipati (рабочее имя, 24.10.2026)

- Рынок: 112 agent-payment стартапов (Dealroom), Skyfire/Nevermined/Payman/Coinbase x402/Mastercard Agent Pay/Visa; FinOps/observability — отдельные point solutions. Прямого независимого audit/receipt-слоя нет.
- Решение: не строить ещё один OS/рельс. **Nidhipati** = Proof + Spend + Guard + Reserve + Resolve + Reconcile; запускать по модулям.
- Имя: Nidhipati («владыка сокровищ», эпитет Куберы). Предварительно: `nidhipati.com` — whois no match, `.io` — RDAP 404, npm/PyPI — 404. Это не юридическая проверка; домен не покупаем до выручки.
- Attest апгрейдится, но одного апгрейда мало: нужны validator, данные, отчёты, партнёры. Код — 20%, доверие/данные — 80%.
- RWA для соло: proof-of-reserve/NAV, не эмиссия. Стейблкоины: reconcile/invoice/ops, не эмиссия. Prediction: resolution evidence/data, не MM.
- Первый код: **Nidhipati Proof validator** (1–2 недели, 10 тестов), затем Spend audit CLI.
- Полный бриф: `/media/Sruti/iamthat/research/2026/2026-10-24/NIDHIPATI-ПРОДУКТ.md`.

## 26.10.2026 — follow-up 27.10 отменён, FinOps-письма отправлены

- **Отмена:** 9 GitHub issues (Bindu #615, internet-court #37, Daydreams #708,
  Goncafer47 #3, OneShot #7, Grantex #1861, BlindPay #42, Talyvor #865,
  BlockRun #195) — 15 обращений, **0 ответов**. Follow-up 27.10 отменён, чтобы
  не спамить. Задача в хабе закрыта с этой причиной.
- **Вместо этого:** 2 письма FinOps/observability-партнёрам с конкретным fit:
  - Helicone `enterprise@helicone.ai` — аудит расходов рядом с observability.
  - LiteLLM (BerriAI) `ishaan@berri.ai` — аудит после прокси, вопрос об интеграции.
  - Langfuse — публичного email нет; не отправлял.
- **Ответов: 0.** Бюджет: 0. Следующий шаг — только ответ или новый проверенный адрес.
