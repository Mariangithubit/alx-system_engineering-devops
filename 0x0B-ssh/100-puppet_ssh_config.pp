# Setting Client configuration file (w/ Puppet)

file_line { 'Turn off passowrd auth':
  ensure  => present,
  path    => '/etc/ssh/ssh_config',
  line    => '    PasswordAuthentication no',
  replace => true,
}

file_line { 'True identify file':
  ensure  => present,
  path    => '/etc/ssh/ssh_config',
  line    => '    IdentifyAuthentication ~/.ssh/school',
  replace => true,
}
