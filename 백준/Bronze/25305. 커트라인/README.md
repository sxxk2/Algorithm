# [Bronze II] 커트라인 - 25305 

[문제 링크](https://www.acmicpc.net/problem/25305) 

### 성능 요약

메모리: 30840 KB, 시간: 72 ms

### 분류

구현(implementation), 정렬(sorting)

### 문제 설명

<p style="user-select: auto;">2022 연세대학교 미래캠퍼스 슬기로운 코딩생활에 <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative; user-select: auto;"><mjx-math class="MJX-TEX" aria-hidden="true" style="user-select: auto;"><mjx-mi class="mjx-i" style="user-select: auto;"><mjx-c class="mjx-c1D441 TEX-I" style="user-select: auto;"></mjx-c></mjx-mi></mjx-math><mjx-assistive-mml unselectable="on" display="inline" style="user-select: auto;"><math xmlns="http://www.w3.org/1998/Math/MathML" style="user-select: auto;"><mi style="user-select: auto;">N</mi></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext" style="user-select: auto;">$N$</span></mjx-container>명의 학생들이 응시했다.</p>

<p style="user-select: auto;">이들 중 점수가 가장 높은 <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative; user-select: auto;"><mjx-math class="MJX-TEX" aria-hidden="true" style="user-select: auto;"><mjx-mi class="mjx-i" style="user-select: auto;"><mjx-c class="mjx-c1D458 TEX-I" style="user-select: auto;"></mjx-c></mjx-mi></mjx-math><mjx-assistive-mml unselectable="on" display="inline" style="user-select: auto;"><math xmlns="http://www.w3.org/1998/Math/MathML" style="user-select: auto;"><mi style="user-select: auto;">k</mi></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext" style="user-select: auto;">$k$</span></mjx-container>명은 상을 받을 것이다. 이 때, 상을 받는 커트라인이 몇 점인지 구하라.</p>

<p style="user-select: auto;">커트라인이란 상을 받는 사람들 중 점수가 가장 가장 낮은 사람의 점수를 말한다.</p>

### 입력 

 <p style="user-select: auto;">첫째 줄에는 응시자의 수 <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative; user-select: auto;"><mjx-math class="MJX-TEX" aria-hidden="true" style="user-select: auto;"><mjx-mi class="mjx-i" style="user-select: auto;"><mjx-c class="mjx-c1D441 TEX-I" style="user-select: auto;"></mjx-c></mjx-mi></mjx-math><mjx-assistive-mml unselectable="on" display="inline" style="user-select: auto;"><math xmlns="http://www.w3.org/1998/Math/MathML" style="user-select: auto;"><mi style="user-select: auto;">N</mi></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext" style="user-select: auto;">$N$</span></mjx-container>과 상을 받는 사람의 수 <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative; user-select: auto;"><mjx-math class="MJX-TEX" aria-hidden="true" style="user-select: auto;"><mjx-mi class="mjx-i" style="user-select: auto;"><mjx-c class="mjx-c1D458 TEX-I" style="user-select: auto;"></mjx-c></mjx-mi></mjx-math><mjx-assistive-mml unselectable="on" display="inline" style="user-select: auto;"><math xmlns="http://www.w3.org/1998/Math/MathML" style="user-select: auto;"><mi style="user-select: auto;">k</mi></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext" style="user-select: auto;">$k$</span></mjx-container>가 공백을 사이에 두고 주어진다.</p>

<p style="user-select: auto;">둘째 줄에는 각 학생의 점수 <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative; user-select: auto;"><mjx-math class="MJX-TEX" aria-hidden="true" style="user-select: auto;"><mjx-mi class="mjx-i" style="user-select: auto;"><mjx-c class="mjx-c1D465 TEX-I" style="user-select: auto;"></mjx-c></mjx-mi></mjx-math><mjx-assistive-mml unselectable="on" display="inline" style="user-select: auto;"><math xmlns="http://www.w3.org/1998/Math/MathML" style="user-select: auto;"><mi style="user-select: auto;">x</mi></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext" style="user-select: auto;">$x$</span></mjx-container>가 공백을 사이에 두고 주어진다.</p>

### 출력 

 <p style="user-select: auto;">상을 받는 커트라인을 출력하라.</p>

