# Naron-Py

Team. NARU & 나루 : 커뮤니티

NARU에서 운영 하는 공식 봇입니다.

project - 나론_Naron-Py

라이브러리 - Nextcord [Python]

Kor-Disccord-BOT_C_2021

## 안내사향
이봇은 이 제작자의 개인 디스코드 봇이며 그외에 다른 사용자에게는 서버에 넣을수있는 링크를 배포를 하지 않을것이며
이점에서 주의 하여주시기 바람니다

# 기능

## 주요 작동 서비스
Embed
Message Component
접두사 명령어 [ ! or = ]
슬래시 명령어 [ / ]

## 봇 입장시 안내 문구 (EMbed)
나를 이방에 초대 해줘서 고마워! 이방에 나를 작동되개하는 법을 안내해 줄깨!

일단 나의 명령어 접두사는 ! or = 가 있어 하지면 그래도 슬레시(/) 명령어가 있다고!
시작 명령어는 'setup' 이나 '셋업' 을 접두사나 슬래시를 붙어서 치면 자동으로 작동해

그리고 나는 명령어를 사용하면 버튼과 메뉴 선택이라는 기능을 주로 작동되
추가적인 명령어를 보고싶으면 'help' 를 치면 나에게 있는 명령어들이 다 나와!

## 기본 작동 서비스
핑 상태 [ping, 핑]
봇 정보 
명령어 안내 [help]
트위치 방송 알림
유튜브 업로드 알림
봇 DM으로 건의 사항 발송시 관리자에게 해당 메시지 전송

## 주요 작동 서비스
### 역활 지급 시스템 [명령어는 관리자 전용 명령어]
[Embed, Message Component(Select Menu)]
기타 게임권한요청
※기타 게임 추가요청은 5인이상 플레이하시는분이 있어야 추가가 가능합니다.
요청시 [관리자 언급] 으로 문의부탁드립니다.

아래 리스트중 원하시는 역할을 선택하여 채널 입장권한을 얻어주세요.
-권한이 있는상태로 클릭시 해당 권한은 제거됩니다.

### 입장시 인증 명령어 
단. 메시지가 봇을 추가 했을때 전송 되거나 인증이 되개끔 가면서 안될경우 추방이 안되도록 해야된다.

명령어는 !인증 [캡차인증 코드]

### 로그 기능
통화방, 채팅방, 설정 로그를 어느 채팅방에 설정을 해두면 자동으로 로그가 뜰때마다 올라가개끔 해주는 식
ex) Logger#6088랑 기능 비슷한 느낌으로 가도 좋음
명령어 [setchannel]

설정 관련 로그
channelCreate, channelUpdate, channelDelete, guildBanAdd, guildBanRemove, guildRoleCreate, guildRoleDelete, guildRoleUpdate, guildUpdate

통화방 관련 로그
voiceChannelJoin, voiceStateUpdate, voiceChannelSwitch, voiceChannelLeave

채팅방 관련 로그
messageDelete, messageDeleteBulk, messageUpdate

채널 설정
대시보드는 가장 쉬운 설정 방법입니다! Setchannel은 봇 로깅 동작을 구성합니다.

예:
%setchannel <- 이것이 전송된 모든 것을 기록합니다.
%setchannel messageDelete, messageUpdate <- 메시지 삭제 및 업데이트 기록
%setchannel guildMemberAdd, guildMemberRemove, guildMemberKick <- 로그인, 탈퇴, 시작
%setchannel anyevent <- 기록할 이벤트를 하나씩 설정합니다. 다중에는 쉼표를 사용합니다. 유효한 이벤트:
channelCreate, channelUpdate, channelDelete, guildBanAdd, guildBanRemove, guildRoleCreate, guildRoleDelete, guildRoleUpdate, guildUpdate, messageDelete, messageDeleteBulk, messageUpdate, guildMemberAdd, guildMemberKick, guildMemberRemove, guildMemberUpdate, voiceChannelLeave, voiceChannelJoin, voiceStateUpdate, voiceChannelSwitch, guildMemberNickUpdate, guildMemberVerify, guildEmojisUpdate, guildMemberBoostUpdate

stoplogging
특정(또는 모든) 이벤트를 기록하지 않도록 하려면 로그 채널에서 이것을 사용하십시오. 이 명령은 setchannel의 반대이며 이벤트를 설정하는 대신 설정 해제하는 데 동일한 방식으로 사용할 수 있습니다.

예:
%stoplogging <- 사용된 채널에 기록하도록 구성된 모든 이벤트 기록을 중지합니다.
%stoplogging messageDelete, messageUpdate <- 봇이 이것이 사용된 채널에 messageDelete 및 messageUpdate를 기록했다면 이제 설정 해제됩니다.
%stoplogging guildMemberVerify <- 봇이 이것이 사용된 채널에 회원 확인 이벤트를 기록했다면, 그렇게 하지 않을 것입니다.

### 채팅 청소 [청소, prune]

사용시 뜨는 문구

00개의 메세지(들)을/를 삭제하고 있어요... 잠시 기다려주세요.

삭제 완료시

완료! 아래에 결과를 표시할게요.

Embed

정리결과

모든 메시지를 삭제했어요
```숫자```

오래된 메시지들을 삭제했어요
```숫자```

유저에 의해 메시지가 삭제되었어요
```
kileu#0001 : 숫자
```

자동 삭제 기능이 작동되었어요. 10초후 메시지를 삭제할꺼에요. 'c'를 눌러 취소할 수 있어요
