# Security---Study
모의해킹 독학 및 보안 공부 기록용 저장소
정보보안기사 실기 합격 후, 실무 능력을 갖춘 모의해커가 되기 위한 기록 공간입니다.

## 📅 학습 목표
- 웹 기본 구조 및 웹 언어(HTML, JS, SQL, PHP) 정복
- 파이썬을 활용한 해킹 도구 제작 기초 다지기
- 드림핵(Dreamhack) 워게임 격파

## 🛠️ 기술 스택 (Learning)
- **Language:** Python, JavaScript, SQL
- **OS:** Linux (Ubuntu, Kali), Windows
- **Tool:** Burp Suite, Wireshark



모의해킹 취업 대비 3개월 집중 로드맵 (Daily 5H)
<p>[ 1개월차: 기초 인프라 및 언어 적응기 ]
목표: 코드 독해력 확보 및 터미널 환경 익숙해지기</p style="margin-bottom:30px;">

시간 배분:
<br>
웹 기초 (2.5H): 생활코딩 HTML → JS → SQL(PHP병행) 순으로 핵심 태그와 쿼리문 위주 공부
<br>

<p>cf) CSS 중요내용
id (#) / class (.) : 특정 HTML 요소를 지칭할 때 사용 (JS와 연동됨)
display: none;	: 화면에는 안 보이지만 HTML 소스에는 존재하는 요소 찾기
z-index	 : 투명한 레이어를 씌워 클릭을 유도할 때 (낚시 사이트 제작)
<style> 태그	 : HTML 내부에 CSS가 삽입되는 위치 파악
</p>
파이썬 (1.5H): 제어문/함수 정복 후 구글링 없이 가위바위보 게임 구현 (혼공파 활용)</p>
<br>
리눅스 (1H): OverTheWire Bandit 1~15단계 (명령어 grep, find, awk 숙달)</p>
<br>
<p>[ 2개월차: 웹 취약점 원리 및 도구 숙달 ]
목표: 주요 취약점 메커니즘 이해 및 드림핵 입문</p style="margin-bottom:30px;">
<br>
시간 배분:
<br>
웹 해킹 (2.5H): 드림핵 Web Hacking 로드맵 진입 (Server-side 공격 집중)
<br>
패킷 분석 (1.5H): Burp Suite 설치 및 HTTP Request/Response 패킷 변조 실습
<br>
자동화 기초 (1H): 파이썬 requests 모듈로 웹 서버에 자동 요청 보내기 실습
<br>
<p>[ 3개월차: 실전 워게임 및 기술 문서화 ]
목표: 독립적인 문제 해결 및 모의해킹 보고서 작성 기초 확보</p style="margin-bottom:30px;">
<br>
시간 배분:
<br>
워게임 (2.5H): 드림핵 Web Level 1~2 문제 풀이 및 Client-side (XSS, CSRF) 학습
<br>
취약점 분석 (1.5H): 공격 성공 후 소스코드 상의 취약점 발생 원인(Root Cause) 분석
<br>
문서화 (1H): 깃허브에 기술적인 Write-up 작성 및 보안 대책(Remediation) 정리
<br>
<p style="margin-top:10px;">⚠️ T의 행동 강령 (필독)
눈으로 공부 금지: 무조건 타이핑하고, 에러 메시지를 직접 마주하라.
<br>
기록에 매몰 금지: 깃허브 정리는 하루 마지막 20분 내로 끝내라.
<br>
병행의 원칙: 정보보안기사 결과와 상관없이 이 루틴을 유지하라. 실습이 곧 최고의 시험 공부다.</p style="margin-bottom:50px:">



<p>1. 🛑 지금은 건너뛰어도 되는 것 (프레임워크/상태관리)</p>
React, Next.js: 웹을 더 편하게 만들기 위한 '도구(프레임워크)'입니다. 해킹의 기초 원리를 배울 때는 오히려 복잡함만 더합니다. 나중에 웹해킹 숙련자가 되었을 때 "최신 웹 기술의 허점"을 찾기 위해 공부해도 늦지 않습니다.
<br>
<br>
Redux: 데이터를 관리하는 복잡한 도구입니다. 지금은 전혀 모르셔도 해킹 공부에 지장 없습니다.
<br>
<br>
<p>2. ✅ 꼭 들어야 하거나 고민해볼 것</p>
① JavaScript (기본)<br>
필수입니다. React 같은 도구 말고, 'Vanilla JavaScript'라고 불리는 순수 자바스크립트 문법(변수, 함수, 조건문, DOM 조작 등) 강의만 들으세요.
<br>
이걸 알아야 XSS(Cross Site Scripting) 공격 원리를 이해할 수 있습니다.
<br>
② Ajax<br>
강력 추천합니다. 페이지 새로고침 없이 서버와 데이터를 주고받는 기술입니다.
<br>
요즘 웹사이트는 대부분 Ajax를 쓰기 때문에, 중간에서 데이터를 가로채는 해킹 실습을 할 때 이 개념을 모르면 막막할 수 있습니다.
<br>
③ Node.js vs PHP (선택의 갈림길)<br>
둘 다 '서버 언어'입니다.
<br>
PHP: 전통적인 웹 해킹의 교과서입니다. 모의해킹 입문용 워게임이나 자료가 압도적으로 많습니다. (입문자에게 추천!)
<br>
Node.js: 자바스크립트로 서버를 만드는 최신 기술입니다. PHP 대신 이걸 배워도 되지만, 입문 자료를 찾기가 PHP보다 조금 더 어려울 수 있습니다.
<br>
결정: 처음에 정했던 대로 PHP를 먼저 파시는 걸 추천합니다. 하나를 알면 나머지는 금방 배웁니다.
<br>
<p style="margin-top:10px;> "3. 모의해킹 공부를 위한 '생활코딩' 핵심 요약</p>
지금 단계에서는 아래 리스트만 정복한다는 마음으로 진행하세요.
<br>
WEB1 - HTML & Internet (완료 단계)
<br>
WEB2 - CSS (핵심만 빠르게)
<br>
WEB2 - JavaScript (기본 문법 + DOM 조작까지만)
<br>
WEB2 - Ajax (데이터가 어떻게 오가는지 파악)
<br>
WEB2 - PHP (서버 로직 이해)
<br>
Database - MySQL (데이터 추출 이해)
