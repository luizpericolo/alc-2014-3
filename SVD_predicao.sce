n=5
k=3
for (i=1:n)
    soma=0
    media=0
    for (j=1:n)
        soma=soma+R(i,j)
        media=soma/n
        for(b=1:n)
            Cmedia(i,b)=media
        end
        Rnorm(i,:)=R(i,:)-media
    end
end

[U S V]= svd(R)

Sk=zeros(k,k)
for (i=1:k)
    Sk(i,i)=S(i,i)
    Uk(:,i)=U(:,i)
    Vk(:,i)=V(:,i)
end

Rk = Uk*Sk*Vk'

Ck= Uk*(sqrt(Sk))' 
Pk= sqrt(Sk)*Vk'

Cpred = Cmedia + Ck * Pk
