from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return '''
    <h1>👩‍💻 About Me</h1>
    <p>Hello! I’m a passionate <strong>DevOps Enthusiast</strong> with a strong interest in automation, cloud, and CI/CD tools.</p>
    <p>Explore the pages: <a href="/skills">Skills</a> | <a href="/projects">Projects</a> | <a href="/contact">Contact</a></p>
    '''

@app.route('/skills')
def skills():
    return '''
    <h1>🛠️ DevOps Skills</h1>
    <ul>
        <li>Linux Fundamentals</li>
        <li>Git & GitHub</li>
        <li>Docker & Kubernetes</li>
        <li>Ansible & Terraform</li>
        <li>Jenkins & GitHub Actions</li>
        <li>AWS, Python, Bash</li>
    </ul>
    <a href="/">Back to Home</a>
    '''

@app.route('/projects')
def projects():
    return '''
    <h1>📁 Projects</h1>
    <ol>
        <li><strong>Ansible Cluster Setup</strong></li>
        <li><strong>Dockerized Web Scraper</strong></li>
        <li><strong>File Manager using Python</strong></li>
    </ol>
    <a href="/">Back to Home</a>
    '''

@app.route('/contact')
def contact():
    return '''
    <h1>📬 Contact Me</h1>
    <p><strong>Email:</strong> vaibhavi.sugandhi03@gmail.com</p>
    <p><strong>LinkedIn:</strong> <a href="https://linkedin.com/in/vaibhavisugandhi">linkedin.com/in/vaibhavisugandhi</a></p>
    <a href="/">Back to Home</a>
    '''

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
