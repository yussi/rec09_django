from django import forms

class TimeFreeRecordForm(forms.Form):
    channel = forms.CharField(label="放送局", required=True)
    t_ft = forms.DateTimeField(label="録音開始時間", required=True)
    t_to = forms.DateTimeField(label="録音終了時間", required=True)

    def form_valid(self, form):
        messages.success('データ入力成功')
        return redirect('recfile:index')
