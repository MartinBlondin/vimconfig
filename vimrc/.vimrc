"" vundle
set nocompatible
filetype off

set rtp+=~/.vim/bundle/Vundle.vim/
call vundle#begin()
    
Plugin 'VundleVim/Vundle.vim'
Plugin 'tpope/vim-fugitive'
Plugin 'scrooloose/nerdtree'
Plugin 'klen/python-mode'
Plugin 'davidhalter/jedi-vim'

call vundle#end()

filetype plugin indent on

" Leader
let mapleader=","

" Nerdtree setup
map <F2> :NERDTreeToggle<CR>

" Python-mode setup
let g:pymode_rope = 0

" colourscheme
syntax on
colorscheme monokai
set nofoldenable

" set working directory to current file's directory
set autochdir

" tab settings
set tabstop=4
set shiftwidth=4
set expandtab

" line numbers
set number
set relativenumber

" bracket autocompletion
inoremap " ""<left>
inoremap ' ''<left>
inoremap ( ()<left>
inoremap [ []<left>
inoremap { {}<left>
inoremap {<CR> {<CR>}<ESC>O

" Use ctrl-[hjkl] to select the active split!
nmap <silent> <c-k> :wincmd k<CR>
nmap <silent> <c-j> :wincmd j<CR>
nmap <silent> <c-h> :wincmd h<CR>
nmap <silent> <c-l> :wincmd l<CR>]"

" autoindent inside of bracket
:set autoindent
:set cindent

" highlight characters past column 90
augroup vimrc_autocmds
    autocmd!
    autocmd FileType python highlight Excess ctermbg=DarkGrey guibg=Black
    autocmd FileType python match Excess /\%90v.*/
    autocmd FileType python set nowrap
augroup END