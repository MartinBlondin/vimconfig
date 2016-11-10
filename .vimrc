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
Plugin 'tpope/vim-surround'

call vundle#end()

filetype plugin indent on

" Leader
let mapleader=","

" LaTeX

" Nerdtree setup
map <F2> :NERDTreeToggle<CR>

" Python-mode setup
let g:pymode_rope = 0

" colourscheme
syntax on
colorscheme molokai
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

" using bc to calculate
nmap <Leader>c :r ! echo "" \| bc 6<Left>

" rendering with <leader>l
autocmd FileType markdown nmap <Leader>l :w<ENTER> :! pandoc -o <c-R>%<BS><BS>pdf --template assignment <c-R>%<ENTER><ENTER>
autocmd FileType python nmap <Leader>l :w<ENTER> :! python3 <c-R>%<ENTER>
autocmd FileType tex nmap <Leader>l :w<ENTER> :! pdflatex <c-R>%<ENTER><ENTER>

xmap " S"
xmap ' S'
xmap ( S)
xmap [ S]
xmap { S}

" Prefrences
set noswapfile
