# Bucle for historial

{% for i in range(0,3) %}
{% if session['history'][i] != "" %}
<li>
    <a href="{{ url_for(session.history[i]) }}">{{ session.history[i] }}</a>
</li>
{% endif %}
{% endfor %}