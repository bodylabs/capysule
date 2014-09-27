$venv_dir = '.venv'
$mac_os = `uname -s`.strip == 'Darwin'

desc "Create a Python virtualenv"
task :create_venv do
    raise unless system("virtualenv #{$venv_dir}")
end

task :require_venv_activated do
    next if ENV.has_key? 'CI'
    unless File.exists? "#{$venv_dir}/bin/activate"
        puts
        puts "Please create a virtual environment."
        puts
        puts "\t$ rake create_venv"
        puts
        raise
    end
    if ENV['VIRTUAL_ENV'] != File.join(Dir.pwd, $venv_dir)
        puts
        puts "Please activate virtualenv."
        puts
        puts "\t$ . #{$venv_dir}/bin/activate"
        puts
        raise
    end
end

desc "Install dependencies for development"
task :install => :require_venv_activated do
    raise unless system("pip install -r requirements_dev.txt")
end

desc "Install dependencies for distribution"
task :install_dist => :install do
    if $mac_os
        raise unless system("brew update")
        raise unless system("brew tap phinze/cask")
        raise unless system("brew install brew-cask")
        raise unless system("brew cask install pandoc")
    else
        puts
        puts "You must install:"
        puts
        puts " - pandoc"
        puts
        raise
    end
end

def command_is_in_path?(command)
    system("which #{ command} > /dev/null 2>&1")
end

task :test => :require_venv_activated do
    if command_is_in_path?('foreman')
        maybe_foreman_run = 'foreman run'
    else
        maybe_foreman_run = ''
    end
    raise unless system("#{maybe_foreman_run} nosetests -s")
end

desc "Remove .pyc files"
task :clean do
    system("find . -name '*.pyc' -delete")
end

desc "Remove venv and built distributions"
task :veryclean => :clean do
    system("rm -rf ./#{$venv_dir} dist/")
end

task :sdist do
    unless command_is_in_path?('pandoc')
        puts
        puts "Please install pandoc."
        puts
        raise
    end
    raise unless system("python setup.py sdist")
end
