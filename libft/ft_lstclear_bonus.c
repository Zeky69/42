/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_lstclear.c                                      :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: zakburak <zakburak@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/10/31 16:16:22 by zakburak          #+#    #+#             */
/*   Updated: 2025/10/31 16:25:30 by zakburak         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "libft.h"

void	ft_lstclear(t_list **lst, void (*del)(void *))
{
	t_list	*current;
	t_list	*next_node;

	if (lst && del)
	{
		current = *lst;
		while (current)
		{
			next_node = current->next;
			ft_lstdelone(current, del);
			current = next_node;
		}
		*lst = NULL;
	}
}
