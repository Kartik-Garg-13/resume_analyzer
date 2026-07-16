document.getElementById('analyze-btn').addEventListener('click', function() {
    
    const file = document.getElementById('resume-input').files[0]
    const role = document.getElementById('role-select').value

    if (!file) {
        alert('Please upload a resume PDF')
        return
    }

    if (!role) {
        alert('Please select a role')
        return
    }

    const formData = new FormData()
    formData.append('resume', file)
    formData.append('role', role)
    const btn = document.getElementById('analyze-btn')
    btn.textContent = 'Analyzing...'
    btn.disabled = true

    fetch('/analyze', {
        method: 'POST',
        body: formData
    })
    .then(response => response.json())
    .then(data => {
        if (data.error) {
            alert(data.error)
            btn.textContent = 'Analyze Resume'
            btn.disabled = false
            return
        }
        
        document.getElementById('percentage').textContent = data.match_percentage + '%'
        document.getElementById('role-label').textContent = 'Match for ' + data.role

        const foundList = document.getElementById('found-list')
        const missingList = document.getElementById('missing-list')
        
        foundList.innerHTML = ''
        missingList.innerHTML = ''

        data.found.forEach(skill => {
            const li = document.createElement('li')
            li.textContent = skill
            li.className = 'found-item'
            foundList.appendChild(li)
        })

        data.missing.forEach(skill => {
            const li = document.createElement('li')
            li.textContent = skill
            li.className = 'missing-item'
            missingList.appendChild(li)
        })

        document.getElementById('result').classList.remove('hidden')

        btn.textContent = 'Analyze Resume'
        btn.disabled = false
    })
}) 