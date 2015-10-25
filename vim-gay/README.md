# vim-gay (based on Vim 7.4)


## 파일관련
- html 파일을 열고 `:!open %`하면 바로 브라우져를 실행할 수 있다!
- **`.vimrc` 수정 후 콘솔에서 `source ~/.vimrc`하는 대신 `:so %`하면 된다!**
- `<CTRL-^>`: 이전 열었던 파일 열기 (CTRL+6을 의미함. 원래 <CTRL> 키와 조합된 문자 표기시엔 대문자로 표기)
- `vim -d file1 file2`: file1과file2의 차이점 비교
- `:x`는 `:up`+`:q`와 같다. `:wq` 대신 `x` 권장.
- `:w`로 저장하면 변경사항 없더라도 디스크 I/O. 변경사항 있을때만 저장하는 `:up` 권장.
- 복사하기(`y`)하면 `~/.viminfo` 파일에 레지스터(임시 버퍼)를 기록
- `ps -ef | vim -`하면 `ps -ef`의 결과물을 모두 Vim으로 읽을 수 있음. '-'는 표준 입력을 의미. 명령 결과가 길거나, 실행 결과를 편집해야할 때 유용.
- `:ls` 혹은 `:files`: 버퍼(파일) 목록 보기. => Vim에서는 편집 중인 문서를 버퍼(buffer)라고 부르며, 문서를 불러와서 보거나 작업하는 기억장치라는 의미로 사용됩니다.
- `gf`, `<CTRL-W> f`, `<CTRL-W> gf`: 본문의 파일명을 인식해서 열어주는 명령어(ex `#include <stdio.h>`위에서 `gf`누르면 시스템 헤더 파일 찾아서 열어줌), (ex `./test_vim-workshop-master/README.md`위에 커서를 두고 `gf`)
- `gf`의 검색 대상 디렉터리를 추가하고 싶으면 `set path+=~/directory_name` => `.vimrc`에 저장해두면 편하게 사용할 수 있음.


## 창분할관련
- `[#]<CTRL-W> v` 하면 현재 보고 있는 화면을 [#]행만큼 주고 vertically split. 다른 행을 동시에 보고 있을때 유용. (물론 `[#]<CTRL-W> s`도 존재)
- `[#]gt`, `[#]gT`: #만큼 tab 이동
- `:sp`(split), `:vs`(vertical split)
- `<CTRL-W> w`: 다음 창으로 이동 
- `<CTRL-W> p`: 이전 창으로 이동


## 편집기술
- 숫자 위에서 `<CTRL-A>`: +1 (16진수나 8진수에서도 가능. ex. 16진수=>0x0a, 8진수=>010)
- 숫자 위에서 `<CTRL-X>`: -1 (16진수나 8진수에서도 가능)
- `H`, `L`, `M`: 맨 위/아래/가운데로 커서 이동.
- `0`(or `^`), `$`: 맨 앞/뒤으로 커서 이동
- `{`, `}`: `\n\n` 나오는 곳. 즉 문단 끝과 처음으로 이동.
- `w`, `e`, `b`: 단어 단위로 이동
- `W`, `E`, `B`: 의미 단어 단위로 이동
- `d$`: `d`를 누르면 `$`를 받을때까지 대기 상태(pending)인데, 이 상태 operation pending 모드라고 한다. 
- `dj`, `dk`: 커서 기준으로 아래 위 문장을 합쳐버림. (부합하지 않는 녀석들은 삭제!)
- `diw`, `daw`: 커서 위치 상관없이 단어 삭제. `daw`의 경우 space까지 제거. (`:help diw`)
```
	"dl"	delete character (alias: "x")		|dl|
	"diw"	delete inner word			*diw*
	"daw"	delete a word				*daw*
	"diW"	delete inner WORD (see |WORD|)		*diW*
	"daW"	delete a WORD (see |WORD|)		*daW*
	"dgn"   delete the next search pattern match    *dgn*
	"dd"	delete one line				|dd|
	"dis"	delete inner sentence			*dis*
	"das"	delete a sentence			*das*
	"dib"	delete inner '(' ')' block		*dib*
	"dab"	delete a '(' ')' block			*dab*
	"dip"	delete inner paragraph			*dip*
	"dap"	delete a paragraph			*dap*
	"diB"	delete inner '{' '}' block		*diB*
	"daB"	delete a '{' '}' block			*daB*
```
- `d}`, `d{`: 현재 커서부터 문단 끝까지 삭제. 문단 처음까지 삭제.
- `~/.vimrc`에 약어 설정하기
```
ab hunjae@ hunjae@ab180.co
ab pdb@ import pdb; pdb.set_trace()
ia time0@ <C-R>=strftime("%Y.%m.%d-%H:%M:%S")<CR>
ia time1@ <C-R>=strftime("%c")<CR>
```


## 문자열 찾기/교체
- `:.,$s/이전문자열/바꿀문자열/gc`: 현재 라인부터 search and replace (y/n)


## Tips for Linux
- 셸에서 `man ascii`: 전체 ASCII 테이블 관람


## References
- http://vimawesome.com/
- [Markdown Preview for Vim](https://github.com/shime/vim-livedown)
- [Vim+Tmux workshop](https://github.com/nicknisi/vim-workshop)


## Livedown

```
" launch the Livedown server and preview your markdown file
:LivedownPreview

" stop the Livedown server
:LivedownKill

" launch/kill the Livedown server
:LivedownToggle
```
