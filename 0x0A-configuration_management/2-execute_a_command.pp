# Kills a process
exec { 'kill_process_killmenow':
  command => 'pkill -f "killmenow"',
  onlyif  => 'pgrep -f "killmenow"',
}

