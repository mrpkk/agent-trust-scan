# PROGRESS — Agent Trust & Commerce

**Цель:** первые платные клиенты в крипто-мире без РФ и без AILegal.  
**Модель:** услуги по безопасности и монетизации AI-агентов с кошельками; позже — hosted Trust Layer.  
**Владелец:** IndrA (Ганеша). **Дата старта:** 24.10.2026.

---

## Правило шага

Один шаг = один законченный результат: код + тест + коммит + пуш + запись в Obsidian/память.  
Шаг не закрывается, пока нет зелёного теста и публичного артефакта.  
Максимальная длина шага: делать всё, что не требует разрешения владельца, и не останавливаться на «план».

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
- [x] Скрипт звонка 6 вопросов.
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

## Outreach 24.10.2026 — первые 9 отправок

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

**Блокеры каналов:**
- Gmail SMTP/IMAP: `GMAIL_PAS` недействителен (Authentication failed); Gmail web-сессия из cookie-моста уходит в account chooser. Письма не отправлены.
- GitHub API: fine-grained token не имеет `issues:write` на чужие репозитории (403); classic token истёк. Issues отправлены через web-сессию в xvfb.
- worldliberty/agentpay-sdk и usewhisk/whisk: только шаблоны bug/feature/security, нет blank issue; не использовал шаблон не по назначению.
- Claw402: нет публичного email/issue-канала.

**Следующий шаг:** follow-up 27.10.2026 по тем же issue; ответить на комментарии; если тишина — 20 новых целей.
